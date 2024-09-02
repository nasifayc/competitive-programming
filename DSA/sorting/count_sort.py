def count_sort(arr):
    M = max(arr)
    # print(M)

    freq_array = [0] * (M+1)
    for i in range(len(arr)):
        freq_array[arr[i]] += 1
    index = 0
    for i in range(len(freq_array)):
        while freq_array[i] > 0:
            arr[index] = i
            freq_array[i] -= 1
            index += 1
    print(arr)



count_sort([2,4,7,12,8,12,4])