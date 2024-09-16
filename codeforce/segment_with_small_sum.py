def smallSum(nums, target)-> int:
    result, total, l,r,n = 0,0,0,0,len(nums)
    while r < n:
        total += nums[r]
        while total > target and l <= r:
            total -= nums[l]
            l += 1
        result = max(result, r - l + 1)
        r += 1
    return result


n, m = map(int, input().split())  
arr = list(map(int, input().split()))
result = smallSum(arr, m)

print(result)