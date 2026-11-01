import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np,pandas as pd,json,hashlib,time,sys
from pathlib import Path
from scipy.special import expit,logsumexp
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from numpy.polynomial.hermite import hermgauss
ROOT=Path(__file__).resolve().parents[1]; SRC=Path(os.environ.get('CO2_SOURCE',str(ROOT/'input/observaciones_principal.csv')))
GROUPS=['exclusively_nonfirst_observed','exclusively_first_observed','mixed']
BASE=['Intercept','prior_first','prior_mixed','log2_prior_publications','log2_team_evidence','calendar_decade']
def design(d,m):
    a=(d.prior_signing_group==GROUPS[1]).to_numpy(float); b=(d.prior_signing_group==GROUPS[2]).to_numpy(float)
    x=[np.ones(len(d)),a,b,np.log2(d.n_prior_coauthor_publications_with_identified_partner),np.log2(d.n_authors_evidence_max),(d.outcome_year-2010)/10]; names=BASE.copy()
    if m=='H1':
        z=(d.alter_density.to_numpy()-.5)/.1; x.extend([z,z*a,z*b]);names+=['density_per_0.1','density_x_prior_first','density_x_prior_mixed']
    if m=='H2': x.append((d.burt_constraint_weighted.to_numpy()-.5)/.1);names+=['constraint_per_0.1']
    return np.column_stack(x),names
class GLMM:
    def __init__(self,d,m,k=60):
        self.d=d;self.X,self.names=design(d,m);self.y=(d.signing_role=='first').to_numpy(float);self.g,ids=pd.factorize(d.node_id);self.j,js=pd.factorize(d.work_id);self.G=len(ids);self.J=len(js);self.p=self.X.shape[1]
        self.A=csr_matrix((np.ones(len(d)),(self.g,np.arange(len(d)))),shape=(self.G,len(d)))
        z,w=hermgauss(k);self.z=z*np.sqrt(2);self.lw=np.log(w/np.sqrt(np.pi))
    def fg(self,t,wi=None,wj=None):
        if wi is None:wi=np.ones(self.G)
        if wj is None:v=np.ones(len(self.d))
        else:v=wj[self.j]
        s=np.exp(t[-1]);u=s*self.z
        eta=self.X@t[:-1]; e=eta[:,None]+u[None,:]
        ll=(self.y[:,None]*e-np.logaddexp(0,e))*v[:,None]
        z=self.A@ll+self.lw;li=logsumexp(z,axis=1);post=np.exp(z-li[:,None])
        r=(self.y[:,None]-expit(e))*v[:,None]*post[self.g]*wi[self.g,None]
        grad=np.r_[self.X.T@r.sum(axis=1),(r*u).sum()]
        return -np.dot(wi,li),-grad
    def fit(self,start=None,wi=None,wj=None):
        if start is None:start=np.r_[np.zeros(self.p),np.log(.7)]
        return minimize(self.fg,start,args=(wi,wj),jac=True,method='L-BFGS-B',bounds=[(None,None)]*self.p+[(-7,3)],options={'gtol':1e-6,'ftol':1e-11,'maxiter':400,'maxls':40})
def diagnostics(mod,r):
    fun,g=mod.fg(r.x);return {'success':bool(r.success),'message':str(r.message),'loglik':float(-fun),'sigma':float(np.exp(r.x[-1])),'gradient_max':float(np.max(abs(g))),'iterations':int(r.nit),'rank':int(np.linalg.matrix_rank(mod.X)),'parameters_fixed':mod.p,'condition_X':float(np.linalg.cond(mod.X)),'max_abs_beta':float(max(abs(r.x[:-1]))),'sigma_boundary':bool(r.x[-1]<-6.99 or r.x[-1]>2.99),'min_conditional_p_u0':float(expit(mod.X@r.x[:-1]).min()),'max_conditional_p_u0':float(expit(mod.X@r.x[:-1]).max())}
def run_original():
    d=pd.read_csv(SRC); assert len(d)==1080 and not d.duplicated(['node_id','work_id']).any()
    sourcecols=['node_id','work_id','context_id','outcome_year','signing_role','prior_signing_group','n_prior_coauthor_publications_with_identified_partner','n_authors_evidence_max','alter_density','burt_constraint_weighted','quality_joint_exclusion']
    required=sourcecols[:-1]; valid=d[required].notna().all(axis=1)&d.signing_role.isin(['first','nonfirst'])&d.prior_signing_group.isin(GROUPS)&(d.n_authors_evidence_max>=2)
    sets={'main_to2025':d.outcome_year<=2025,'quality_to2025':(d.outcome_year<=2025)&~d.quality_joint_exclusion,'including2026':np.ones(len(d),bool)}
    rows=[]; diags=[];fits={}; exc=[]
    for sn,mask in sets.items():
        for i in d.index:
            reason='used' if mask[i] and valid[i] else ('missing_or_invalid_required' if mask[i] else ('quality_joint_flag' if sn=='quality_to2025' and d.loc[i,'quality_joint_exclusion'] else 'outcome_after2025'))
            exc.append({'dataset':sn,'node_id':d.loc[i,'node_id'],'work_id':d.loc[i,'work_id'],'reason':reason})
        ds=d[mask&valid].copy().reset_index(drop=True);ds.to_csv(ROOT/'output'/f'data_{sn}.csv',index=False)
        cc=ds.groupby('node_id').context_id.nunique(); pn=ds.groupby('work_id').size()
        counts={'dataset':sn,'researchers':ds.node_id.nunique(),'contexts':ds.context_id.nunique(),'publications':ds.work_id.nunique(),'observations':len(ds),'first':int((ds.signing_role=='first').sum()),'single_context_researchers':int((cc==1).sum()),'repeated_context_researchers':int((cc>=2).sum()),'shared_publications':int((pn>1).sum()),'shared_publication_observations':int(pn[pn>1].sum()),'missing_invalid_exclusions':int((mask&~valid).sum())}
        for m in ['M0','H1','H2']:
            mod=GLMM(ds,m); rs=[]
            for s in [.25,1,2]:
                t=np.zeros(mod.p+1);t[-1]=np.log(s);rs.append(mod.fit(t))
            r=min(rs,key=lambda r:r.fun); dg=diagnostics(mod,r)
            chk=GLMM(ds,m,100);rr=chk.fit(r.x);dg.update({'quadrature100_loglik_change':float(-rr.fun+r.fun),'quadrature100_max_beta_change':float(max(abs(rr.x[:-1]-r.x[:-1]))),'quadrature100_sigma_change':float(np.exp(rr.x[-1])-np.exp(r.x[-1])),'multistart_loglik_range':float(max(z.fun for z in rs)-min(z.fun for z in rs))})
            # 60-point estimates kept only if quadrature is stable
            if dg['quadrature100_max_beta_change']>.01 or abs(dg['quadrature100_loglik_change'])>.01:raise RuntimeError(('quadrature',sn,m,dg))
            diags.append(dict(dataset=sn,model=m,**dg));rows.append(dict(model=m,**counts));fits[f'{sn}|{m}']={'theta':r.x.tolist(),'names':mod.names}
            print(sn,m,json.dumps(dg),flush=True)
    pd.DataFrame(rows).to_csv(ROOT/'output/model_denominators.csv',index=False);pd.DataFrame(diags).to_csv(ROOT/'output/original_diagnostics.csv',index=False);pd.DataFrame(exc).to_csv(ROOT/'output/exclusions_all_rows.csv',index=False)
    (ROOT/'output/original_fits.json').write_text(json.dumps(fits,indent=2)); (ROOT/'input_hashes.json').write_text(json.dumps({str(SRC):hashlib.sha256(SRC.read_bytes()).hexdigest()},indent=2))
if __name__=='__main__':run_original()
