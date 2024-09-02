def sort(arr):
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i,len(arr)):
            count += 1
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print("Number of comparisons:", count)

arr = [10,9,8,7,6]

print(arr)
sort(arr)
print(arr)