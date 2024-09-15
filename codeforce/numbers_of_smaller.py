def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i,j= 0,0
    merged = []

    while j < m:
        if i < n and j < m:
            if arr2[j] > arr1[i]:
                i += 1
            else:
                j += 1
                merged.append(i)
        else:
            j += 1
            merged.append(i)
        
    return merged






n, m = map(int, input().split())  
arr1 = list(map(int, input().split()))  
arr2 = list(map(int, input().split()))  


result = merge(arr1, arr2)
print(" ".join(map(str, result)))