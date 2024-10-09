class Solution:
    def quickSort(self, arr,s,e):
        if s >= e:
            return
        
        pivot = arr[e]
        left = s

        for i in range(s,e):
            if arr[i] < pivot:
                arr[i],arr[left] = arr[left], arr[i]
                left += 1
        
        arr[left],arr[e] = arr[e],arr[left]

        # self.quickSort(arr, s, left-1)
        # self.quickSort(arr,left+1,e)


if __name__ == '__main__':
    solution = Solution()
    arr = [5, 2, 8, 1, 3, 9, 4, 6, 7]
    solution.quickSort(arr, 0, len(arr)-1)
    print(arr)