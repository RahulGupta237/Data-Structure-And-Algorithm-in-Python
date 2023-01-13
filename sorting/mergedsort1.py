

"""


step 1: start

step 2: declare array and left, right, mid variable

step 3: perform merge function.
    if left > right
        return
    mid= (left+right)/2
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge(array, left, mid, right)

step 4: Stop


MergeSort(arr[], l,  r)
If r > l

Find the middle point to divide the array into two halves: 
middle m = l + (r – l)/2
Call mergeSort for first half:   
Call mergeSort(arr, l, m)
Call mergeSort for second half:
Call mergeSort(arr, m + 1, r)
Merge the two halves sorted in steps 2 and 3:
Call merge(arr, l, m, r)


"""


def merge(arr,left,mid,right):
    l=mid-left+1
    r=right-mid
    leftArray=[0]*l
    rightArray=[0]*r
    """

    This Function through Int object is not subscritable
    
    
    """

    for i in range(0,l):
        leftArray=arr[l+i]

    for j in range(0,r):
        rightArray=arr[mid+1+j]

    i=j=k=0
    while i < l and j < r:
        if leftArray[i] <= rightArray[j]:
            arr[k] = leftArray[i]
            i += 1
        else:
            arr[k] = rightArray[j]
            j += 1
        k += 1

		# Checking if any element was left
    while i < l:
        arr[k] = leftArray[i]
        i += 1
        k += 1

    while j < r:
        arr[k] = rightArray[j]
        j += 1
        k += 1

    return arr

def mergeSort(arr,left,right):
    if left<right:
        mid=(left+(right-1)//2)
        """
         mergeSort for first half:   
Call mergeSort(arr, l, m)
Call mergeSort for second half:
Call mergeSort(arr, m + 1, r)
Merge the two halves sorted in steps 2 and 3:
Call merge(arr, l, m, r)
        """
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)
    return arr

arrlist=[12,11 ,13, 5 ,6 ,7 ]
right=0
left=(len(arrlist))
x=mergeSort(arrlist,right,left)
print(f"Wooow Great {x}")




