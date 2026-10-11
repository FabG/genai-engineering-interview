"""Regenerate original teaching plots: python generate_plots.py (requires matplotlib)."""
from pathlib import Path
import math
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'axes.titlesize':16,'axes.labelsize':13,
                    'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False,
                    'figure.facecolor':'#f8fafc','axes.facecolor':'#f8fafc','text.color':'#24364b',
                    'axes.labelcolor':'#24364b','xtick.color':'#24364b','ytick.color':'#24364b'})
TEAL='#087f8c'; BLUE='#3b5bdb'; ORANGE='#d97706'; GRAY='#cad3df'
rng=np.random.default_rng(2026)

def save(fig,name,title,desc,foot):
    fig.suptitle(title,fontsize=20,fontweight='bold',x=.04,ha='left')
    fig.text(.04,.025,foot,fontsize=11,color='#52647a')
    fig.tight_layout(rect=(.025,.075,.98,.91))
    path=OUT/(name+'.svg')
    fig.savefig(path,metadata={'Title':title,'Description':desc,'Creator':'Original repository illustration'})
    s=path.read_text().replace("font-family: 'DejaVu Sans'", "font-family: Arial, Helvetica, sans-serif")
    from html import escape
    s=re.sub(r'<svg\b([^>]*)>',r'<svg\1 role="img" aria-labelledby="chart-title chart-desc">',s,count=1)
    pos=s.index('>',s.index('<svg'))+1
    s=s[:pos]+f'\n<title id="chart-title">{escape(title)}</title><desc id="chart-desc">{escape(desc)}</desc>'+s[pos:]
    path.write_text(s);plt.close(fig)

fig,ax=plt.subplots(figsize=(11,4.6))
for row,n in enumerate([4,6,8]):
    for col in range(12):
        color=TEAL if col<n else ORANGE if col==n else BLUE if col<n+3 else '#e8edf3'
        ax.add_patch(Rectangle((col,row),.94,.7,facecolor=color))
        label='Train' if col==1 else 'Gap' if col==n else 'Valid.' if col==n+1 else ''
        if label: ax.text(col+.45,row+.35,label,ha='center',va='center',fontsize=11,color='white')
ax.set(xlim=(-.1,12),ylim=(-.2,2.9),xticks=np.arange(12)+.45,xticklabels=np.arange(1,13),yticks=[.35,1.35,2.35],yticklabels=['Fold 1','Fold 2','Fold 3'],xlabel='Month →')
ax.invert_yaxis();ax.spines[['left','bottom']].set_visible(False);ax.tick_params(length=0)
save(fig,'time-validation','Evaluate on the future, using only the past','Three expanding training windows, each with one gap month and two later validation months.','Illustrative folds. Gap and horizon must match label availability and the deployment task.')

fig,ax=plt.subplots(figsize=(10,4.8))
ax.barh(['Region','Tenure','Recent activity'],[.005,.08,.13],xerr=[.006,.012,.018],color=[GRAY,TEAL,BLUE],capsize=6)
ax.axvline(0,color='#52647a',lw=1);ax.set(xlabel='Decrease in held-out accuracy after shuffling',xlim=(-.015,.18))
save(fig,'permutation-importance','Feature importance depends on the fitted model','Synthetic accuracy decreases: region 0.005, tenure 0.08, recent activity 0.13; error bars show hypothetical variation.','Synthetic repeated-permutation variation; these are not confidence intervals or causal effects.')

# An analytic illustrative ROC curve passes through (FPR=.05, TPR=.8).
power=math.log(.8)/math.log(.05);tpr=np.linspace(0,1,600);fpr=tpr**(1/power);prevalence=.01
precision=np.divide(prevalence*tpr,prevalence*tpr+(1-prevalence)*fpr,out=np.ones_like(fpr),where=(tpr+fpr)>0)
point_precision=.008/(.008+.0495)
fig,axs=plt.subplots(1,2,figsize=(12,5))
axs[0].plot(fpr,tpr,color=TEAL,lw=3);axs[0].plot([0,1],[0,1],'--',color=GRAY)
axs[0].scatter([.05],[.8],color=ORANGE,s=70,zorder=4);axs[0].annotate('FPR 5%, recall 80%',(.05,.8),xytext=(.19,.6),arrowprops={'arrowstyle':'->'},fontsize=12)
axs[0].set(xlabel='False-positive rate',ylabel='True-positive rate (recall)',title='ROC view')
axs[1].plot(tpr,precision,color=BLUE,lw=3);axs[1].axhline(prevalence,color=GRAY,ls='--')
axs[1].scatter([.8],[point_precision],color=ORANGE,s=70,zorder=4);axs[1].annotate('Precision ≈ 14%',(.8,point_precision),xytext=(.31,.51),arrowprops={'arrowstyle':'->'},fontsize=12)
axs[1].set(xlabel='Recall',ylabel='Precision',title='PR view at 1% prevalence')
for ax in axs:ax.set(xlim=(0,1),ylim=(0,1.03))
save(fig,'roc-pr','One ranking, two views of its operating tradeoff','Synthetic ROC and PR curves share an operating point with recall 0.8, FPR 0.05, and precision about 0.139 at one-percent prevalence.','Analytic illustration, not measured model performance. Threshold selection still requires an error-cost decision.')

fig,ax=plt.subplots(figsize=(9,5.3))
x=np.array([.1,.3,.5,.7,.9]);y=np.array([.04,.14,.28,.43,.64])
ax.plot([0,1],[0,1],'--',color=GRAY,label='Ideal calibration');ax.plot(x,y,'o-',color=ORANGE,lw=3,label='Synthetic bin averages')
ax.set(xlim=(0,1),ylim=(0,1),xlabel='Mean predicted probability',ylabel='Observed positive fraction');ax.legend(loc='upper left',frameon=False)
save(fig,'calibration','Ranking ability does not guarantee calibrated probabilities','A synthetic reliability curve is below the diagonal, indicating overconfidence in the displayed bins.','Bin sizes and uncertainty are omitted in this teaching sketch; include them in an actual evaluation.')

fig,ax=plt.subplots(figsize=(10,4.8));a=np.linspace(0,np.pi,80)
ax.scatter(np.cos(a)+rng.normal(0,.025,80),np.sin(a)+rng.normal(0,.025,80),color=TEAL,s=23,label='Intended group A')
ax.scatter(1-np.cos(a)+rng.normal(0,.025,80),.45-np.sin(a)+rng.normal(0,.025,80),color=BLUE,s=23,label='Intended group B')
ax.scatter([-1.3,2.35,1.25],[-.5,1,1.5],color=ORANGE,s=70,marker='x',label='Isolated observations')
ax.set(xlabel='Feature 1 (scaled)',ylabel='Feature 2 (scaled)');ax.legend(frameon=False,loc='upper right',fontsize=11)
save(fig,'density-clustering','Some clusters are connected regions, not compact balls','Two synthetic crescent-shaped point groups and three isolated observations.','Colors show intended geometry, not fitted DBSCAN labels. Density parameters and representation still matter.')

fig,axs=plt.subplots(1,3,figsize=(13,4.8));x=np.linspace(-2,2,90)
patterns=[rng.normal(0,.28,90),.65*(x*x-1.35)+rng.normal(0,.22,90),rng.normal(0,.08+.22*(x+2),90)]
for ax,y,title in zip(axs,patterns,['No obvious pattern','Curved mean','Changing spread']):
    ax.scatter(x,y,s=14,color=TEAL);ax.axhline(0,color=GRAY,ls='--');ax.set(xlabel='Fitted value',title=title,ylim=(-2.8,2.8))
axs[0].set_ylabel('Residual')
save(fig,'residual-diagnostics','Inspect what the residuals still contain','Three synthetic residual plots: random scatter, curvature, and widening error variance.','Illustrative diagnostics; check dependence, influential observations, and held-out predictive performance too.')

fig,ax=plt.subplots(figsize=(9,4.6));p=np.array([1,1]);q=np.array([4,3]);s=p+.4*(q-p)
ax.plot([p[0],q[0]],[p[1],q[1]],'--',color=GRAY,lw=3)
ax.scatter([p[0],q[0]],[p[1],q[1]],color=TEAL,s=140,label='Observed minority points')
ax.scatter([s[0]],[s[1]],color=ORANGE,s=180,marker='*',label='Synthetic point, λ = 0.4')
ax.set(xlim=(.4,4.6),ylim=(.4,3.7),xlabel='Numeric feature 1',ylabel='Numeric feature 2');ax.legend(frameon=False,loc='upper left',fontsize=11)
save(fig,'smote','SMOTE interpolates; it does not create independent evidence','A synthetic point lies forty percent of the way between two minority examples.','Oversample only training folds; preserve natural prevalence in validation and test data.')

fig,ax=plt.subplots(figsize=(11,4.8));rows=['Baseline','Queueing regression','Prefill regression'];left=np.zeros(3)
for vals,label,color in [([.2,1.2,.2],'Queue',ORANGE),([.6,.6,1.6],'Prefill',BLUE),([1,1,1],'Decode',TEAL)]:
    ax.barh(rows,vals,left=left,label=label,color=color);left+=np.array(vals)
ax.set(xlabel='Illustrative latency in seconds',xlim=(0,3.1));ax.invert_yaxis();ax.legend(frameon=False,ncols=3,loc='lower center',bbox_to_anchor=(.5,1.0))
save(fig,'context-latency','The same latency increase can have different causes','Synthetic total latency rises from 1.8 to 2.8 seconds because of either queueing or prefill, with decoding fixed.','Matched-request teaching example; real systems also have network, retrieval, validation, and other stages.')

fig,ax=plt.subplots(figsize=(9,5));coverage=np.array([.2,.35,.5,.7,.85,1]);risk=np.array([.015,.03,.055,.1,.15,.22])
ax.plot(coverage,risk,'o-',color=TEAL,lw=3);ax.scatter([.7],[.1],color=ORANGE,s=90,zorder=4)
ax.annotate('70 answered; 7 wrong\nper 100 requests',(.7,.1),xytext=(.28,.17),arrowprops={'arrowstyle':'->'},fontsize=12)
ax.set(xlim=(0,1.02),ylim=(0,.26),xlabel='Coverage: fraction answered',ylabel='Error rate among answered cases')
save(fig,'risk-coverage','Measure both answering rate and accepted-answer error','A synthetic selective-risk curve marks 70-percent coverage and 10-percent error among accepted answers.','Hypothetical informative acceptance score. At zero coverage, conditional error is undefined.')

fig,ax=plt.subplots(figsize=(10,4.8));complexity=np.linspace(0,1,100)
ax.plot(complexity,.07+.53*np.exp(-4*complexity),color=TEAL,lw=3,label='Training error')
ax.plot(complexity,.07+.53*np.exp(-4*complexity)+.08+.45*complexity**2,color=BLUE,lw=3,label='Validation error')
ax.set(xlabel='Model complexity →',ylabel='Prediction error',xticks=[],yticks=[]);ax.legend(frameon=False)
ax.text(.03,.12,'Underfit',transform=ax.transAxes);ax.text(.73,.75,'Overfit',transform=ax.transAxes)
save(fig,'generalization','Training fit and generalization can diverge','Illustrative training error falls with complexity while validation error eventually rises.','Conceptual curves, not a universal law: data, optimization, regularization, and model family change their shapes.')

fig,ax=plt.subplots(figsize=(9,5));u=rng.normal(0,1.2,130);v=rng.normal(0,.18,130)
x=(u-v)/np.sqrt(2);y=(u+v)/np.sqrt(2);ax.scatter(x,y,color=TEAL,s=18,alpha=.65)
ax.arrow(-1.9,-1.9,3.8,3.8,width=.025,head_width=.18,color=BLUE,length_includes_head=True)
ax.arrow(.5,-.5,-1,1,width=.02,head_width=.15,color=ORANGE,length_includes_head=True)
ax.text(1.25,1.85,'PC1',color=BLUE);ax.text(-.9,.45,'PC2',color=ORANGE)
ax.set(xlabel='Centered feature 1',ylabel='Centered feature 2',xlim=(-2.7,2.7),ylim=(-2.7,2.7));ax.set_aspect('equal')
save(fig,'pca-directions','PCA rotates toward directions of input variance','Synthetic correlated data with a long first principal direction and a perpendicular second direction.','Directions are illustrative; PCA explains input variance, which is not necessarily predictive signal.')

fig,axs=plt.subplots(1,3,figsize=(13,4.6));logits=np.array([2,1.2,.5,-.2]);labels=['A','B','C','D']
for ax,temp in zip(axs,[.5,1,2]):
    probs=np.exp(logits/temp-max(logits/temp));probs/=probs.sum()
    ax.bar(labels,probs,color=[TEAL,BLUE,ORANGE,GRAY]);ax.set(title=f'Temperature {temp:g}',ylim=(0,1),xlabel='Candidate token')
axs[0].set_ylabel('Sampling probability')
save(fig,'temperature','Temperature reshapes probabilities before sampling','Identical synthetic logits yield a sharper distribution at temperature 0.5 and a flatter one at temperature 2.','No top-k or top-p filtering here. Lower temperature does not establish factual correctness.')
print('Generated 12 original SVG plots.')
