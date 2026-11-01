"""Read frozen observations/outputs, summarize and redraw. No estimation or simulation."""
from pathlib import Path
import hashlib, json, platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os
R = Path(os.environ['CO2_BUILD_ROOT'])
O = R / '05_audit/model_outputs'
T = R / '02_exploratory_tables'
F = R / '03_manuscript_figures'
for p in [T,F]: p.mkdir(exist_ok=True)
sources=json.loads((R/'source_inventory.json').read_text())
for s in sources:
    assert hashlib.sha256((R/s['package_path']).read_bytes()).hexdigest()==s['sha256'],s['package_path']
datasets=['main_to2025','quality_to2025','including2026']
labels={'main_to2025':'Main, through 2025','quality_to2025':'Joint quality restriction, through 2025','including2026':'Including 2026'}
groups=['exclusively_nonfirst_observed','exclusively_first_observed','mixed']
group_labels=['Previously non-first only','Previously first only','Previously mixed']
tables={}
def save(name,df):
    tables[name]=df
    df.to_csv(T/(name+'.csv'),index=False)
den=pd.read_csv(O/'model_denominators.csv')
save('Table_1_sample_denominators',den.loc[den.model.eq('M0')].drop(columns='model'))
desc=[]; signing=[];coverage=[]
vars_context=['n_collaborators','n_prior_coauthor_publications_with_identified_partner','alter_density','burt_constraint_weighted','effective_size_weighted','share_repeat_pair_events']
expected={'main_to2025':(1079,292,717,765,352),'quality_to2025':(791,253,553,590,265),'including2026':(1080,292,718,766,353)}
for ds in datasets:
    d=pd.read_csv(R/'01_samples'/f'data_{ds}.csv')
    c=d.drop_duplicates('context_id'); w=d.drop_duplicates('work_id')
    assert (len(d),d.node_id.nunique(),len(c),len(w),int(d.signing_role.eq('first').sum()))==expected[ds]
    assert not d.duplicated(['node_id','work_id']).any()
    for v in vars_context:
        assert d.groupby('context_id')[v].nunique(dropna=False).max()==1,v
    assert d.groupby('work_id').n_authors_evidence_max.nunique(dropna=False).max()==1
    for v,unit,s in [(v,'researcher-year context',c[v]) for v in vars_context]+[('n_authors_evidence_max','publication',w['n_authors_evidence_max']),('outcome_year','eligible researcher-publication observation',d.outcome_year)]:
        s=pd.to_numeric(s,errors='coerce');q=s.quantile([.25,.5,.75])
        desc.append(dict(dataset=ds,variable=v,unit=unit,n=int(s.count()),missing=int(s.isna().sum()),mean=s.mean(),sd=s.std(),min=s.min(),q25=q.loc[.25],median=q.loc[.5],q75=q.loc[.75],max=s.max()))
    for g in groups:
        sub=d[d.prior_signing_group.eq(g)];n=len(sub);nf=int(sub.signing_role.eq('first').sum())
        signing.append(dict(dataset=ds,prior_group=g,observations=n,first=nf,nonfirst=n-nf,first_proportion=nf/n))
    for v in ['position_independently_checked','team_partial','quality_joint_exclusion','quality_partial_ego_document','quality_provisional_alter']:
        flag=d[v].astype(str).str.lower().isin(['true','1'])
        coverage.append(dict(dataset=ds,flag=v,unit='eligible researcher-publication observation',flagged=int(flag.sum()),denominator=len(d),proportion=flag.mean()))
    coverage.append(dict(dataset=ds,flag='reference_membership',unit='eligible researcher-publication observation',flagged=int(d.membership.eq('reference').sum()),denominator=len(d),proportion=d.membership.eq('reference').mean()))
save('Table_2_descriptives',pd.DataFrame(desc))
save('Table_3_signing_history',pd.DataFrame(signing))
save('Table_S1_documentary_coverage',pd.DataFrame(coverage))
save('Table_4_GLMM_coefficients_POINT_ONLY',pd.read_csv(O/'coefficients.csv')[['dataset','model','term','beta','OR']])
save('Table_5_indicator_slopes_POINT_ONLY',pd.read_csv(O/'hypothesis_slopes.csv')[['dataset','model','prior_group','beta_per_0.1','OR_per_0.1']])
pc=pd.read_csv(O/'probability_contrasts.csv')[['dataset','model','prior_group','low','high','n_standardization_rows','p_low','p_high','delta_high_minus_low']]
pc['difference_percentage_points']=100*pc.delta_high_minus_low
save('Table_6_standardized_probabilities_POINT_ONLY',pc)
save('Table_S2_random_intercept_SD_POINT_ONLY',pd.read_csv(O/'fit_statistics.csv')[['dataset','model','sigma_researcher']])
curves=pd.read_csv(O/'prediction_curves.csv')[['dataset','model','prior_group','indicator','value','probability','observed_min','observed_max']]
save('Figure_source_points_NO_INTERVALS',curves)
colors=['#196b86','#b55a1b','#6d5a9a']; styles=['-','--',':']
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,'svg.fonttype':'none'})
for model,indicator,xlabel in [('H1','alter_density','Prior alter density'),('H2','burt_constraint_weighted','Prior weighted Burt constraint')]:
    fig,axs=plt.subplots(1,3,figsize=(12.6,4.6),sharey=True)
    for ax,g,title in zip(axs,groups,group_labels):
        for ds,color,style in zip(datasets,colors,styles):
            sub=curves[(curves.model==model)&(curves.dataset==ds)&(curves.prior_group==g)].sort_values('value')
            ax.plot(sub.value,sub.probability,color=color,linestyle=style,linewidth=2,label=labels[ds])
        ax.set(title=title,xlabel=xlabel,ylim=(0,1));ax.grid(axis='y',alpha=.2)
        assert len(ax.collections)==0  # No ribbons or interval artists.
    axs[0].set_ylabel('Standardized probability of first authorship')
    fig.legend(*axs[0].get_legend_handles_labels(),loc='lower center',bbox_to_anchor=(.5,.08),ncol=3,frameon=False,fontsize=9)
    fig.suptitle('Exploratory GLMM predictions',fontsize=14)
    fig.text(.5,.025,'Point estimates only. Calibrated uncertainty intervals are not supplied.',ha='center',fontsize=10)
    fig.subplots_adjust(bottom=.27,top=.84,wspace=.12)
    for ext in ['png','pdf','svg']:fig.savefig(F/f'{model}_predictions_POINT_ONLY.{ext}',dpi=220)
    plt.close(fig)

def md_table(df):
    def fmt(x):
        if isinstance(x,(float,np.floating)): return f'{x:.4f}'
        return str(x).replace('|','/')
    return '| '+' | '.join(df.columns)+' |\n| '+' | '.join(['---']*len(df.columns))+' |\n'+'\n'.join('| '+' | '.join(fmt(x) for x in row)+' |' for row in df.itertuples(index=False,name=None))+'\n'
notes={
'Table_1_sample_denominators':'Counts are sample-specific; first counts eligible first-author rows. Context = researcher-year. Model labels H1/H2 identify unchanged specifications, not hypothesis decisions.',
'Table_2_descriptives':'Prior indicators use one row per researcher-year context, avoiding repetition by current publication. Team size uses one row per publication and maximum recovered documentary evidence. SD is descriptive dispersion, not a standard error. Effective size and repetition remain descriptive; no predictors were added.',
'Table_3_signing_history':'Prior categories use usable recovered signatures within the preceding three years, not complete careers. The unit and denominator are eligible researcher-publication observations.',
'Table_4_GLMM_coefficients_POINT_ONLY':'Conditional working-model coefficients and odds ratios. Previously non-first only is the reference. No standard errors, confidence intervals or tests are supplied.',
'Table_5_indicator_slopes_POINT_ONLY':'Slopes per 0.1 indicator unit, combining interaction coefficients for H1. H2 has one common constraint slope. These are exploratory conditional associations.',
'Table_6_standardized_probabilities_POINT_ONLY':'Original main-sample quartile endpoints are retained across sensitivities where supported. H1 standardizes within prior category; H2 pooled contrast standardizes over all observations. Probabilities integrate over a new researcher intercept and use sample-specific empirical covariates. No interval interpretation.',
'Table_S1_documentary_coverage':'Retained source flags, not a new quality adjudication. Independent positional verification is narrower than analytical usability.',
'Table_S2_random_intercept_SD_POINT_ONLY':'Sigma is the SD of the researcher intercept in log-odds units, a working-model heterogeneity parameter; it is neither a coefficient SE nor a leadership measure.',
'Figure_source_points_NO_INTERVALS':'Exact saved point curves with uncertainty columns omitted; source for the new figures.'}
parts=['# CO2 drafting tables\n\nFrozen exploratory results. All values derive from archived data and fits. CSV files retain numerical precision; displayed values are rounded to four decimals.\n']
for name,df in tables.items():
    if name=='Figure_source_points_NO_INTERVALS':continue
    parts.extend(['\n## '+name+'\n\n'+notes[name]+'\n\n',md_table(df)])
(T/'TABLES_FOR_DRAFTING.md').write_text(''.join(parts))
(T/'TABLE_NOTES.json').write_text(json.dumps(notes,indent=2))
checks={'source_files_verified':len(sources),'sample_counts':expected,'original_inputs_and_outputs_unchanged':True,'fits_executed':0,'simulations_executed':0,'manuscript_figure_intervals':False,'python':platform.python_version(),'pandas':pd.__version__,'numpy':np.__version__,'matplotlib':matplotlib.__version__}
(R/'05_audit/release_checks.json').write_text(json.dumps(checks,indent=2))
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(R.rglob('*')) if p.is_file() and p.name!='release_manifest.json'}
(R/'release_manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(checks,indent=2))
