class Solution:
    def mergeSort(self, arr, start, end):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)
    
    def merge(self, arr, start, mid, end):

        temp = []
        left = start
        right = mid + 1

        while (left <= mid and right <= end):
            if arr[right] < arr[left]:
                temp.append(arr[right])
                right += 1
                
            else:
                temp.append(arr[left])
                left += 1
                
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
            
        
        while right <= end:
            temp.append(arr[right])
            right += 1
        
        for i in range(start,end+1):
            arr[i] = temp[i-start]

