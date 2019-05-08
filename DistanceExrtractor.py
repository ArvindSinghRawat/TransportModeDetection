import pandas as pd
import numpy as np
def ExtractDistanceInM(path = 'data/Arvind 2000.csv',export=False):
    file = pd.read_csv(path)
    lat = file['latitude']
    lon = file['longitude']
    lat1 = np.array(lat[1:])
    lat2 = np.array(lat[:-1])
    lon1 = np.array(lon[1:])
    lon2 = np.array(lon[:-1])
    l1 = lat1 - lat2
    l2 = lon1 - lon2
    lat1 = np.array(lat[1:])
    lat2 = np.array(lat[:-1])
    lon1 = np.array(lon[1:])
    lon2 = np.array(lon[:-1])
    l1 = lat1 - lat2
    l2 = lon1 - lon2
    l1 = l1 * l1
    l2 = l2 * l2
    l = l1 + l2
    l = l ** 0.5
    l = l * 111139
    l = pd.DataFrame(l)
    if export == True:
        target = path.split('.')[0]
        l.to_csv(target+'Distance.csv',header=False,index=False)
    return l