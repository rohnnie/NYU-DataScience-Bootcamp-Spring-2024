import numpy as np
d=np.random.randint(1,100,16).reshape(4,4)
row= lambda x : np.sum(x,axis=1)
column= lambda x : np.sum(x.T,axis=1)
rowSum=row(d)
columnSum = column(d)
print(rowSum,columnSum)
