def mergeSort(x) -> list:
    
    # base cases
    if len(x) > 1:
        # split the list
        mid = len(x) // 2
        L = x[:mid]
        R = x[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        
        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                x[k] = L[i]
                i += 1
            else:
                x[k] = R[j]
                j += 1
            k += 1
 
        # checking if any element was left
        while i < len(L):
            x[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            x[k] = R[j]
            j += 1
            k += 1
        
        return x
    else:
        return 0
        
