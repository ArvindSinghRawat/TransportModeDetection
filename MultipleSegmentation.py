import numpy as np
import pandas as pd
import time
from SlidingWindow import SlidingWindowSegmentation
path = 'data/Arvind 2000.csv'
file = pd.read_csv(path)
data = file['speed (m/s)']
start = time.time()
for i in np.percentile(data,[0,10,20,30,40,50,60,70,80,90,100]):
    s1 = time.time()
    s = SlidingWindowSegmentation(file,data,i)
    print("Anchors at ",i," : ",s.get_anchor())
    s2 = time.time()
    print("No. of Anchors at ",i," : ",s.get_anchor_length())
    print("\nTime for ",i," : ",s2-s1,"\n")
print("\nTotal Time : ",time.time()-start)