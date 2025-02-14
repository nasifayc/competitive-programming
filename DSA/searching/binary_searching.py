class Solution:
    def binarySearch(self,arr,s,e,target):
        l = s
        h = e
        while l <= h:
            mid = (l+h)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                h = mid-1
            else:
                l = mid+1
            
        return -1
        
if __name__ == '__main__':
    s = Solution()
    arr = [2, 3, 4, 10,40, 90 ,100 ]
    target = 10
    result = s.binarySearch(arr, 0, len(arr)-1, target)
    print(f'The target {target} is found at index {result}')