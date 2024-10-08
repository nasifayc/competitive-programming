def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i,j= 0,0
    merged = []

    while i < n or j < m:
        if i < n and j < m:
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        elif i < n:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return merged


n, m = map(int, input().split())  
arr1 = list(map(int, input().split()))  
arr2 = list(map(int, input().split()))  


result = merge(arr1, arr2)
print(" ".join(map(str, result)))