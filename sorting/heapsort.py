# initializing a list
numbers = [1, 3, 0, 4, 0, 5, 6, 0, 7]
# moving all the zeroes to end
new_list = [num for num in numbers if num != 0] + [num for num in numbers if num == 0]
# printing the new list
print(new_list)
