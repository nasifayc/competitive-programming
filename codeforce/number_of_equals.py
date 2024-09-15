def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0
    result = 0

    while i < n and j < m:
        if arr1[i] == arr2[j]:
            count1 = 1
            count2 = 1
            i += 1
            j += 1
            
            while i < n and arr1[i] == arr1[i-1]:
                count1 += 1
                i += 1
            
            while j < m and arr2[j] == arr2[j-1]:
                count2 += 1
                j += 1

            
            result += count1 * count2
        
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return result

n, m = map(int, input().split())  
arr1 = list(map(int, input().split()))  
arr2 = list(map(int, input().split()))

result = merge(arr1, arr2)
print(result)  
