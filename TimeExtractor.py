import pandas as pd
import numpy as np
def ExtractTimeInM(path = 'data/Arvind 2000.csv',export=False):
    path = 'data/Arvind 2000.csv'
    file = pd.read_csv(path)
    data = file['time']
    tm = pd.DataFrame(list(data.str.split()))[1]
    tm = pd.DataFrame(list(tm.str.split(':')))
    hr = np.array(list(map(int, tm[0])))
    mn = np.array(list(map(int, tm[1])))
    tm = hr * 60 + mn
    tm = tm - tm.min()
    tm = pd.DataFrame(tm)
    if export == True:    
        target = path.split('.')[0]
        tm.to_csv(target+'Distance.csv',header=False,index=False)
    return tm