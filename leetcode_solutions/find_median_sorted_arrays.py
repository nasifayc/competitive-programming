from typing import List


class Solution:
    def mergeSort(self, arr, low, high):
        if low >= high:
            return arr
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mainArr = nums1 + nums2
        self.mergeSort(mainArr, 0 , len(mainArr)-1)
        n = len(mainArr)
        if(n % 2 == 0):
            m = n//2
            median = (mainArr[m-1] + mainArr[m])/2
            return median
        else:
            m = n//2
            median = mainArr[m]
            return median


        