"""

Bucket sort is mainly useful when input is uniformly distributed over a range. 
For example, consider the following problem. 
Sort a large set of floating point numbers 
which are in range from 0.0 to 1.0 and are uniformly distributed across the range.
 How do we sort the numbers efficiently?


 A simple way is to apply a comparison based sorting algorithm. The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(n Log n), i.e., they cannot do better than nLogn. 
Can we sort the array in linear time? Counting sort can not be applied here as we use keys as index in counting sort. Here keys are floating point numbers.  
The idea is to use bucket sort. Following is bucket algorithm.

"""


# - Create buckets and distribute elements of array into buckets
# - Sort buckets individually
# - Merge buckets after sorting

# - Number of buckets = round(Sqrt(number of elements))
# round(sqrt(9)) = 3
# - Appropriate bucket = ceil(Value * number of buckets / maxValue)
# ceil(5*3/9) = ceil(1.6) = 2

# Python3 program to sort an array
# using bucket sort
import math


def bucketSort(x):
    Number_of_buckets = round(math.sqrt(len(x)))
    max_value=max(x)
    bucket_list=[[] for i in range(1,Number_of_buckets+1)]

     # Put array elements in different buckets 
    for j in x:
        maxValue=max(x)
        Appropriate_bucket_with_index = math.ceil(j * Number_of_buckets / maxValue)
        bucket_list[Appropriate_bucket_with_index-1].append(j)
    for i in range(len(bucket_list)):
        bucket_list[i].sort()  # you can also the call the isertion sort
    
    # merged the bucket

    k=0
    for i in range(len(bucket_list)):
        for j in range(len(bucket_list[i])):
            x[k]=bucket_list[i][j]
            k+=1
    return f"bucket list {bucket_list} and sorted array {x}"
    
    



	

# Driver Code
x = [1,2,3,5,9,7,8,6]
print("Sorted Array is")
print(bucketSort(x))

# This code is contributed by
# Oneil Hsiao
