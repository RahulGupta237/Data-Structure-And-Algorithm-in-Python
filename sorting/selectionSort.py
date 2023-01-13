"""
     The selection sort algorithm sorts an array by 
     repeatedly finding the minimum element 
     (considering ascending order) from the unsorted part and putting it at the beginning. 

The algorithm maintains two subarrays in a given array.

            The subarray which already sorted. 
            The remaining subarray was unsorted.
"""


def selection_sort(unsorted_list):
     """
     Time complexity---O(N^2)
     Space Complexity-- O(1)
     When to use Selection Sort?
               - When we have insu cient memory
               - Easy to implement
     When to avoid Selection Sort?
     -      - When time is a concern

     """
     # Traverse through all array elements
     for i in range(len(unsorted_list)):
          
          # Find the minimum element in remaining
          # unsorted array
          min_idx = i
          for j in range(i+1, len(unsorted_list)):
               if unsorted_list[min_idx] > unsorted_list[j]:
                    min_idx = j
                    
          # Swap the found minimum element with
          # the first element	
          print(min_idx,unsorted_list[min_idx])
          unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]
     sorted_list=unsorted_list
     return sorted_list

A = [64, 25, 12, 22, 11]
x=selection_sort(A)
print(x)


