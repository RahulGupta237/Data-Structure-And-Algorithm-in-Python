"""

is a simple sorting algorithm that works similar
to the way you sort playing cards in your hands. 
The array is virtually split into a sorted and 
an unsorted part. Values from the unsorted part
are picked and placed at the correct position in the sorted part.

"""
def insertionSort(newarr):
        """
        When to use Insertion Sort?
            - When we have insu cient memory
            - Easy to implement
            - When we have continuous inflow of numbers and we want to keep
                them sorted
        When to avoid Insertion Sort?
            - When time is a concern
        
        """
   
        for i in range(1, len(newarr)):

            key = newarr[i]

            # Move elements of newarr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < newarr[j] :
                    newarr[j + 1] = newarr[j]
                    j -= 1
            newarr[j + 1] = key
 


        return newarr
	
    
"""
time complexity O(N^2)
Space complexity O(1)
"""
arrl = [12, 11, 13, 5, 6]
x=insertionSort(arrl)
print(x)


