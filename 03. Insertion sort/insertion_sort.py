#defining insertion sort function
def insertion_sort_func(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j=j-1
        A[j+1] = key
        print('Pass:\t',A)
    return A

list1 = [4,7,2,9,1,6,3,8,5,0]
print('The unsorted list is:\t',list1)
print('The sorted list is:\t',insertion_sort_func(list1))