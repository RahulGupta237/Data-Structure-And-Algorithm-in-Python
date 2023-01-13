
import numpy as np

TwoDarray=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(TwoDarray)

# Searching 2D elements
def Accessing2dArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return f"index[{i}, {j}]"
        print()
    return "No value found"

x=Accessing2dArray(TwoDarray,8)
print(x)