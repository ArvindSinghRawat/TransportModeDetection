import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def norm(x,mean,stddev):
    value = x - mean
    value = value * value
    value = value / 2
    value = value / (stddev ** 2)
    value = - value
    return np.exp(value)
def preprocess(data):
    data = pd.Series(data)
    data = data.dropna()
    data = data.drop_duplicates()
    return data
def stddev(data):
    data = pd.Series(data)
    return data.var() ** 0.5
def init(path="data/Arvind 2000.csv",cname='speed (m/s)',export=False,preprocessed = False,plot= False,removedna=True):
    data = pd.read_csv(path)[cname]
    t = path.split('.')[0]
    t = t.split('/')
    if preprocessed == False:
        data = preprocess(data)
    else:
        if removedna == False:
            data = data.dropna()
    n = norm(data,data.mean(),stddev(data))
    if export == True:
        target = t[0]+'/normed data/'+t[1]+'.csv'
        dc = np.empty_like(data)
        dc = data
        nc = np.empty_like(n)
        nc = n
        res = pd.concat([dc,nc], ignore_index=True,axis=1)
        res.to_csv(target,header=['data','normed data'],index=False)
    if plot == True:
        d = np.array(sorted(data))
        nc = norm(d,d.mean(),stddev(d))
        plt.plot(d,nc)
        text = 'Distribution of '+t[1]
        q = np.percentile(d,[0,25,33,50,66,75,100])
        m1 = plt.vlines(d.mean(),-0.25,1.25,colors='b')
        m2 = plt.vlines(q[3],-0.25,1.25,colors='r')
        m3 = plt.axvspan(q[1], q[5], alpha=0.5, color='red')
        plt.ylim(-0.1,1.1)
        plt.title(text)
        plt.legend([m1,m2,m3],['Mean','Median','IQR'])
        plt.xlabel('Speed in (m/sec)')
        plt.ylabel('Norm(speed)')
    return n