import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
df = pd.read_excel("C:/Users/Hp/Desktop/Dataset/test/SEIT_sem2.xlsx")
df2 = pd.read_excel("C:/Users/Hp/Desktop/Dataset/test/TEIT_sem2.xlsx")

test = pd.merge(df,df2,how='right',on='Name')
test=test.dropna()
test.DS = test.DS.astype(int)
test.CO = test.CO.astype(int)

def getsubjects(data):
    colum = data.columns.values.tolist()
    del colum[0:2]
    return colum
	
	sesubs = getsubjects(df)
tesubs = getsubjects(df2)
nextsub = ["sub1","sub2","sub3","sub4","sub5"]
nextsub = list(nextsub)

from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
subjects = ["ds","cnt"]
sub = pd.DataFrame()
for se,te,new in zip(sesubs,tesubs,nextsub):
    y_hat_avg = []
    i=0
    while i<len(test):
        x = test.loc[i,se]
        y = test.loc[i,te]
        fit2 = SimpleExpSmoothing((x,y)).fit(smoothing_level=0.4,optimized=False)
        y_hat_avg = np.append(y_hat_avg,(fit2.predict())).round()
        i=i+1                      
    sub[new] = y_hat_avg