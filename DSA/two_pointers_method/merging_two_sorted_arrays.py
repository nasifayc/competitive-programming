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


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8, 10]
    merged_array = merge(arr1, arr2)
    print(merged_array) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

