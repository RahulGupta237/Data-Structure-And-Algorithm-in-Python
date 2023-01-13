# accessing a element through arrays

from array import *
arrayName = array('i', [1,2,3,4,5,6,7])
print(arrayName)
def accessElement(array, index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
accessElement(arrayName,3)