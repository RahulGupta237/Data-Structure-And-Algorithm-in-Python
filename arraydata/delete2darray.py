
import numpy as np

TwoDarray=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
newarray=np.delete(TwoDarray,2,axis=0)   # axis=1 collumn delete and axis=0 row delete
print(TwoDarray)
print(f"new array are having \n{newarray}")
