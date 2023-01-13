import array as arr

# creating an integer data type array
x = arr.array('i', [1,2,3,4,5,6,7])

# using the extend function to add an array to the existing array
x.extend([8,9,10])

# printing the new array
print(x)

# 