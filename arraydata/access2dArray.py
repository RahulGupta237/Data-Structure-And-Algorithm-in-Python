
import numpy as np

TwoDarray=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(TwoDarray)
# accessing elemets of two d array
def accessElement(array,rowIndex,ColIndex):
    if rowIndex >= len(array) and ColIndex>=len(array[0]):
        print('There is not any element in this index')
    else:
        print(array[rowIndex][ColIndex])
accessElement(TwoDarray,1,1)


# traversing of two d arrray

def traverse2dArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end="  ")
        print()

traverse2dArray(TwoDarray)