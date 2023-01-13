# Finding an element
from array import *
arrayName = array('i', [1,2,3,4,5,6,7])
print(arrayName)
def searchInArray(array, value):
    
    for i in array: #O(n)
        if i == value:#O(1)
            #return array.index(value)  O(n)# array.index give time complexity worst case O(n^2) total complexity are O(n2 square)
            return True #O(1)   total complexity O(n)
    return "The element does not exist in this array"

x=searchInArray(arrayName,6)
print(x)

# deleting a element
arrayName.remove(7)
print(arrayName)