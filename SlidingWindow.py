import numpy as np
import matplotlib.pyplot as plt
class SlidingWindowSegmentation:
    def __init__( self , file , data , threshold = 10 ):
        self.file = file
        self.threshold = threshold
        self.data = data
        self.data_len = len(data)
        self.anchor = list()
        self.sliding_window( to_plot = True, verbose = False )
        self.anchor_len = len(self.anchor)
    def sliding_window( self , *args , **kwargs ):
        to_plot = False
        verbose = False
        if 'to_plot' in kwargs:
            to_plot = kwargs["to_plot"]
        if 'verbose' in kwargs:
            verbose = kwargs["verbose"]
        current = 0
        anchor = np.array([])
        segment = np.array([])
        anchor = np.append( anchor , int(0) )
        for i in self.data:
            segment  = np.append( segment , i )
            seg_mean = np.mean(   segment )
            seg_var  = np.var(    segment )
            if abs(seg_mean - i) >= self.threshold:
                anchor = np.append( anchor , int(current) )
                if verbose == True:
                    print("\nSegment : \n",segment)
                    print("\tSegment Mean = ",seg_mean)
                    print("\tSegment Var = ",seg_var)
                segment = np.array([])
            current = current + 1
        if anchor[-1] != self.data_len - 1:
            anchor = np.append( anchor , int(self.data_len - 1) )
        self.anchor = anchor
        if to_plot == True:
            self.drawPlot()
    def get_anchor_length(self):
        return self.anchor_len
    def get_data_length(self):
        return self.data_len
    def get_anchor(self):
        return self.anchor
    def drawPlot(self):
        #f1,ax1 = plt.subplots()
        #sns.lineplot(data = self.data,color='blue')
        f3,ax13 = plt.subplots()
        #fg = plt.figure()
        i = 0
        while i <= len(self.anchor)-2:
            x = self.file.loc[self.anchor[i]:self.anchor[i+1],['index','speed (m/s)']]
            plt.plot(x["index"],x["speed (m/s)"],linewidth=1.25)
            i = i + 1
        st = "At "+str(self.threshold)
        f3.suptitle(st)