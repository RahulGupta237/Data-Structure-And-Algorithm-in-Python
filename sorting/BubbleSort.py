"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping 
the adjacent elements if they are in the wrong order. This algorithm is not 
suitable for large data sets as its average and worst-case time complexity 
is quite high


{

    When to use Bubble Sort?
        - When the input is already sorted
        - Space is a concern
        - Easy to implement
When to avoid Bubble Sort?
    - Average time complexity is poor
}

"""


def BubbleSortAlgo(customLIst):
    """
    Time complexity ---O(N^2)
    Space complexity --O(1)
    """
    for i in range(len(customLIst)-1):#O(n)
        for j in range(len(customLIst)-i-1):#O(n)
            if customLIst[j]>customLIst[j+1]:
                customLIst[j],customLIst[j+1]=customLIst[j+1],customLIst[j]
    return customLIst

unsortlist=[4,3,2,6,8,3,22,5,6]
x=BubbleSortAlgo(unsortlist)
print(x)
