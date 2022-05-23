#defining function for selection sort
def selection_sort_func(A):
    for i in range(0,len(A)):   #traverse through all array elements
        small = i               #minimum element in unsorted list
        for j in range(i+1,len(A)):
            if(A[small]>A[j]):
                small = j
        A[i],A[small] = A[small],A[i]   #swap the min element with the first element of unsorted list
        print('Pass:\t',A)              #list after every iteration
    return A

list1 = [4,7,2,9,1,6,3,8,5,0]
print('The unsorted list is:\t',list1)
print('The sorted list is:\t',selection_sort_func(list1))