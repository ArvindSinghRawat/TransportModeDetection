import pandas as pd
import numpy as np
import csv
def desc(path="data/Arvind 2000.csv",cname = "speed (m/s)",export=False):
    data = pd.read_csv(path)[cname]
    d = dict()
    data = data.fillna(0)
    d['Mean'] = data.mean()
    dq = np.percentile(data,(0,25,50,75,100))
    d['Min'] = dq[0]
    d['1Q'] = dq[1]
    d['Median'] = dq[2]
    d['3Q'] = dq[3]
    d['Max'] = dq[4]
    d['Std dev'] = data.var() ** 0.5
    d['Count'] = len(data)
    if export == True:
        t= path.split('.')[0]
        t= t.split('/')
        target = t[0]+'/details/'+t[1]+' Details.csv'
        with open(target, 'w') as f:
            for key in d.keys():
                f.write("%s,%s\n"%(key,d[key]))
    return d