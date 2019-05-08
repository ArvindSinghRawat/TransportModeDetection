import pandas as pd
from SlidingWindow import SlidingWindowSegmentation
path = 'data/Arvind 2000.csv'
cnt = 0
flag = 0
threshold = 5.55
file = pd.read_csv(path)
data = file['speed (m/s)']
s = SlidingWindowSegmentation(file,data,threshold) 
print("Anchors Length = ",s.get_anchor_length())
print("Anchors = \n",s.get_anchor())