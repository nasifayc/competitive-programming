def bigSum(nums, target)-> int:
    result, total, l,r,n = len(nums) + 1,0,0,0,len(nums)
    while r < n:
        total += nums[r]
        while total - nums[l] >= target and l <= r:
            total -= nums[l]
            l += 1
        if total >= target:
            result = min(result, r - l + 1)
        r += 1
    return result if result <= len(nums) else -1

n, m = map(int, input().split())  
arr = list(map(int, input().split()))

# arr = [2, 6, 4, 3, 6, 8, 9]
result = bigSum(arr, m)


print(result)