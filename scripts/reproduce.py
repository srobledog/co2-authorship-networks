"""Reproduce frozen point estimates only. No resampling or new specifications."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,shutil,subprocess,platform,time
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'vendor'))
from fit_models import GLMM,diagnostics,GROUPS
from predict_points import predict_many
import numpy as np
import pandas as pd
import scipy,matplotlib
# Fixed before the reproduction run; absolute tolerances.
TOL={'theta':1e-4,'loglik':1e-6,'probability':1e-5,'table_numeric':1e-12}
sets=['main_to2025','quality_to2025','including2026']
out=R/'results';out.mkdir(exist_ok=True)
report={'tolerances':TOL,'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'pandas':pd.__version__,'matplotlib':matplotlib.__version__},'simulations_run':0,'checks':[]}
def record(name,passed,**kw):
    report['checks'].append(dict(check=name,passed=bool(passed),**kw))
    (out/'reproduction_report.json').write_text(json.dumps(report,indent=2))
    if not passed:raise RuntimeError(name)
for f,h in json.loads((R/'reference/input_checksums.json').read_text()).items():
    record('sha256:'+f,hashlib.sha256((R/f).read_bytes()).hexdigest()==h)
fits=json.loads((R/'reference/original_fits.json').read_text())
old_diag=pd.read_csv(R/'reference/original_diagnostics.csv')
newfits={};diags=[]
for sn in sets:
    d=pd.read_csv(R/'data'/f'data_{sn}.csv')
    for m in ['M0','H1','H2']:
        mod=GLMM(d,m);candidates=[]
        for sigma in [.25,1,2]:
            start=np.zeros(mod.p+1);start[-1]=np.log(sigma);candidates.append(mod.fit(start))
        res=min(candidates,key=lambda x:x.fun);dg=diagnostics(mod,res)
        chk=GLMM(d,m,100).fit(res.x)
        diff=float(np.max(np.abs(res.x-np.array(fits[sn+'|'+m]['theta']))))
        ref=old_diag[(old_diag.dataset==sn)&(old_diag.model==m)].iloc[0]
        record(sn+'|'+m,bool(res.success) and diff<TOL['theta'] and abs(dg['loglik']-ref.loglik)<TOL['loglik'] and max(abs(chk.x[:-1]-res.x[:-1]))<.01 and abs(chk.fun-res.fun)<.01,max_abs_theta_difference=diff,loglik_difference=float(dg['loglik']-ref.loglik),sigma=dg['sigma'],quadrature100_max_beta_difference=float(max(abs(chk.x[:-1]-res.x[:-1]))))
        newfits[sn+'|'+m]={'theta':res.x.tolist(),'names':mod.names};diags.append(dict(dataset=sn,model=m,**dg))
        print('PASS',sn,m,'theta difference',diff,flush=True)
(out/'refitted_models.json').write_text(json.dumps(newfits,indent=2))
pd.DataFrame(diags).to_csv(out/'refitted_diagnostics.csv',index=False)
# Regenerate model tables from REFITTED parameters, never bootstrap outputs.
w=out/'build';w.mkdir(exist_ok=True)
shutil.copytree(R/'data',w/'01_samples',dirs_exist_ok=True)
o=w/'05_audit/model_outputs';o.mkdir(parents=True,exist_ok=True)
tabs=R/'reference/tables'
coeff=[];slopes=[];stats=[];curves=[];contrasts=[]
endpoints=json.loads((R/'reference/contrast_endpoints.json').read_text())
for sn in sets:
 d=pd.read_csv(R/'data'/f'data_{sn}.csv')
 for m in ['M0','H1','H2']:
  f=newfits[sn+'|'+m];t=np.array(f['theta'])
  coeff.extend(dict(dataset=sn,model=m,term=n,beta=float(b),OR=float(np.exp(b))) for n,b in zip(f['names'],t[:-1]))
  stats.append(dict(dataset=sn,model=m,sigma_researcher=float(np.exp(t[-1]))))
  if m=='M0':continue
  col='alter_density' if m=='H1' else 'burt_constraint_weighted'
  for g in (GROUPS if m=='H1' else ['overall']):
   dd=d if g=='overall' else d[d.prior_signing_group==g]
   beta=t[6]+(t[7] if m=='H1' and g==GROUPS[1] else t[8] if m=='H1' and g==GROUPS[2] else 0)
   slopes.append(dict(dataset=sn,model=m,prior_group=g,**{'beta_per_0.1':beta,'OR_per_0.1':np.exp(beta)}))
   vs=endpoints[m+'|'+g];p=predict_many(dd,m,t[None,:],vs,col)[0]
   contrasts.append(dict(dataset=sn,model=m,prior_group=g,low=vs[0],high=vs[1],n_standardization_rows=len(dd),p_low=p[0],p_high=p[1],delta_high_minus_low=p[1]-p[0]))
  for g in GROUPS:
   dd=d[d.prior_signing_group==g];q=dd[col].quantile([.05,.95]);grid=np.linspace(q.iloc[0],q.iloc[1],21);p=predict_many(dd,m,t[None,:],grid,col)[0]
   curves.extend(dict(dataset=sn,model=m,prior_group=g,indicator=col,value=v,probability=pr,observed_min=dd[col].min(),observed_max=dd[col].max()) for v,pr in zip(grid,p))
for name,rows in [('coefficients',coeff),('hypothesis_slopes',slopes),('fit_statistics',stats),('prediction_curves',curves),('probability_contrasts',contrasts)]:pd.DataFrame(rows).to_csv(o/(name+'.csv'),index=False)
den=pd.read_csv(tabs/'Table_1_sample_denominators.csv');den['model']='M0';den.to_csv(o/'model_denominators.csv',index=False)
# Builder re-verifies every staged input and checks sample counts itself.
inv=[dict(package_path=str(p.relative_to(w)),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for folder in [w/'01_samples',o] for p in folder.rglob('*') if p.is_file()]
(w/'source_inventory.json').write_text(json.dumps(inv,indent=2))
subprocess.run([sys.executable,str(R/'scripts/build_tables.py')],env=dict(os.environ,CO2_BUILD_ROOT=str(w)),check=True)
for refpath in sorted(tabs.glob('*.csv')):
 a=pd.read_csv(refpath);b=pd.read_csv(w/'02_exploratory_tables'/refpath.name)
 tol=TOL['table_numeric'] if refpath.name.startswith(('Table_1','Table_2','Table_3','Table_S1')) else TOL['probability']
 pd.testing.assert_frame_equal(a,b,check_exact=False,atol=tol,rtol=0)
 record('table:'+refpath.name,True,absolute_tolerance=tol,rows=len(a))
figures=list((w/'03_manuscript_figures').glob('*'))
record('figures',len(figures)==6 and all(p.stat().st_size>1000 for p in figures))
report['status']='PASS';report['original_models_refitted']=9;report['scope']='Frozen analytical samples to point estimates, tables and figures. No upstream network reconstruction or inference calibration.'
(out/'reproduction_report.json').write_text(json.dumps(report,indent=2))
print('ALL CHECKS PASSED',flush=True)
