"""

The Merge Sort algorithm is a sorting algorithm that is based on the 
Divide and Conquer paradigm. In this algorithm, the array is initially
 divided into two equal halves and then they are combined in a sorted manner.

Merge Sort Working Process:
    Think of it as a recursive algorithm continuously
    splits the array in half until it cannot be further divided. 
    This means that if the array becomes empty or has only one element left, 
    the dividing will stop, i.e. it is the base case to stop the recursion. 
    If the array has multiple elements, split the array into halves and recursively 
    invoke the merge sort on each of the halves. Finally, when both halves are sorted, 
    the merge operation is applied. Merge operation is the process of
    taking two smaller sorted arrays and combining them to eventually make a larger one.


"""


# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print(f"Sorted array is: {arr}", end="\n")
	printList(arr)

# This code is contributed by Mayank Khanna
