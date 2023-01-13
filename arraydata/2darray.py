import numpy as np

TwoDarray=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(TwoDarray)
newarr=np.insert(TwoDarray,2,[[8,7,0,1]],axis=0)
print(newarr)