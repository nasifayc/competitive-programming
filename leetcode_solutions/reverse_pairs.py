class Solution:
    def __init__(self):
        self.count = 0

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.countPairs(arr, low, mid, high)
        self.merge(arr, low, mid, high)

    def countPairs(self, arr, low, mid, high):
        right = mid + 1
        for left in range(low, mid + 1):
            while right <= high and arr[left] > 2 * arr[right]:
                right += 1
            self.count += right - (mid + 1)  

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

       
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def reversePairs(self, nums: list[int]) -> int:
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.count
