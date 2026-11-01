from fit_models import *
def predict_many(ds,m,ts,values,column):
    # Integrated new-investigator prediction, standardized to FIXED empirical rows.
    X,names=design(ds,m); z,w=hermgauss(100);z=z*np.sqrt(2);w=w/np.sqrt(np.pi)
    ret=np.zeros((len(ts),len(values)))
    idx=6; first=X[:,1];mixed=X[:,2]
    for j,t in enumerate(ts):
        eta=X@t[:-1]; s=np.exp(t[-1]); curves=[]
        for v in values:
            v=(v-.5)/.1
            if m=='H1':
                old=X[:,idx];de=(v-old)*(t[6]+first*t[7]+mixed*t[8])
            else:de=(v-X[:,idx])*t[6]
            curves.append((expit((eta+de)[:,None]+s*z[None,:])@w).mean())
        ret[j]=curves
    return ret
