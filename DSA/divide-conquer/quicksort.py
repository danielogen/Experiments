def quickSort(arr) -> list:
    l = 0
    h = len(arr)
    
    
def partition(A, l, h):
    pivot = A[l]
    i = l
    j = h
    while i < j:
        while A[i] <= pivot:
            i = i + 1
        while A[j] > pivot:
            j = j + 1
        if i < j :
            swap(A[i], A[j])
    swap[A[l], A[j]]

    return j

def swap(a, b):
    temp = a
    a = b
    b =temp

            

