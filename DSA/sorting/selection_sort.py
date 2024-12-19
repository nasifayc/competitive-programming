class Solution:
    def selection_sort(self, nums):
        n = len(nums)
        c = 0
        for i in range(n):
            j = i + 1;
            while j < n - 1:
                c += 1
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1

        print(c)

if __name__ == '__main__':
    solution = Solution()
    nums = [64, 34, 25, 12, 22, 11, 90]
    print('Unsorted array:', nums)
    solution.selection_sort(nums)
    print('Sorted array:', nums)