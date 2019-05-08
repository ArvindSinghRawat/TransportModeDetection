import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
threshold = 0.5
class SlidingWindowSegmentation:
    def __init__( self , data ):
        self.data = data
        self.data_len = len(data)
        self.anchor = list()
        self.sliding_window( 10 , to_plot = False )
        self.anchor_len = len(self.anchor)
    def sliding_window( self , window_size = 10 , *args , **kwargs ):
        to_plot = False
        if 'to_plot' in kwargs:
            to_plot = kwargs["to_plot"]
        if to_plot == True:
            if 'plot_step' in kwargs:
                plot_step = kwargs["plot_step"]
            else:
                plot_step = 2
        flag = 1
        current = 0
        anchor = np.array([])
        segment = np.array([])
        anchor = np.append( anchor , int(0) )
        for i in self.data:
            segment = np.append( segment , i )
            seg_mean = np.mean(segment )
            seg_var  = np.var( segment )
            if seg_var >= threshold:
                anchor = np.append( anchor , int(current) )
                segment = np.array([])
            current = current + 1
        if anchor[-1] != self.data_len - 1:
            anchor = np.append( anchor , int(self.data_len - 1) )
        self.anchor = anchor
    def get_anchor_length(self):
        return self.anchor_len
    def get_data_length(self):
        return self.data_len
    def get_anchor(self):
        return self.anchor
    
path = 'ArvindlargeoutLabelled.csv'
file = pd.read_csv(path)
data = file['speed (m/s)']
s = SlidingWindowSegmentation(data) 
cnt = 0
flag = 0
print(s.get_anchor_length())
print(s.get_anchor())
f1,ax1 = plt.subplots()
sns.lineplot(data = data,color='red')
f2,ax11 = plt.subplots()
print(data[int(s.anchor[0]):int(s.anchor[0+1])])
d = pd.DataFrame(data[int(s.anchor[0]):int(s.anchor[0+1])])
print(list(range(int(s.anchor[0]),int(s.anchor[0+1]))))
i = list(range(int(s.anchor[0]),int(s.anchor[0+1])))
sns.lineplot(data=d,color='red')
f3,ax13 = plt.subplots()
new = list()
i = 0
while i < len(s.anchor)-1:
    d = np.array(data[ int(s.anchor[i]) : int(s.anchor[i+1]) ])
    ind = np.array(list(range(int(s.anchor[i]),int(s.anchor[i+1]))))
    #print(d)
    new.append(d)
    d = np.vstack((ind,d))
    if flag == 0:
        flag = 1
        sns.lineplot(data = file[['latitude','longitude']][ int(s.anchor[i]) : int(s.anchor[i+1]) ],legend = False)
    else:
        flag = 0
        sns.lineplot(data = file[['latitude','longitude']][ int(s.anchor[i]) : int(s.anchor[i+1]) ],legend = False)   
    i = i + 1
print(new)