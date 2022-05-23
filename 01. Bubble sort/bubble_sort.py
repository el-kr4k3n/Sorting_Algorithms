#defining function
def bubble_sort_func(A):
    for i in range(len(A)-1,0,-1):
        #print('i',i)
        for j in range(i):          
            if(A[j]>A[j+1]):
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        print("Pass\t",A)
    return A

list1 = [4,7,2,9,1,6,3,8,5,0]
print("The unsorted list is:\t",list1)
print("The sorted list is:\t",bubble_sort_func(list1))