def numberOfBigSum(nums, target)-> int:
    result, total, l,r,n = 0,0,0,0,len(nums)
    while r < n:
        total += nums[r]
        while total >= target and l <= r:
            total -= nums[l]
            l += 1
        result += l
        r += 1
    return result

n, m = map(int, input().split())  
arr = list(map(int, input().split()))

# arr = [2, 6, 4, 3, 6, 8, 9]
result = numberOfBigSum(arr, m)


print(result)