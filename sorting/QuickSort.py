def swap(my_list, index1, index2):
    my_list[index1],  my_list[index2] = my_list[index2],  my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    print("ist step pivot ",pivot_index)
    print(pivot_index)
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            print(f"swap index is {swap_index} {i}")
            swap(my_list, swap_index, i)
            print(my_list[swap_index],my_list[i])
            print(my_list)
            print("end process")
        else:
            print("number is not swap due to ", f"{my_list[i]} < {my_list[pivot_index]}",pivot_index,i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        print("KKKKKKKKKKKKKKKKKKKKKKKKKK")
        print()

        print(pivot_index)

        print("before calling",my_list)
        quicksort_helper(my_list, left, pivot_index-1)
        print("after calling",my_list)
        quicksort_helper(my_list, pivot_index+1, right)
        print(my_list)
        print()
        print("KKKKKKKKKKKKKKKKKKKKKKKKKK")
    return my_list

def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list)-1)

my_list = [3,5,0,6,2,1,4,77,98,56,3,00]
print("*********************")
print(my_list)
print(quicksort(my_list))

