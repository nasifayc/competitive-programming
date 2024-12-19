class Solution:
    def bubble_sort(self, nums):
        n= len(nums)
        c = 0
        for i in range(n):
            for j in range(n-1-i):
                c += 1
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        print(c)

if __name__ == '__main__':
    solution = Solution()
    nums = [64, 34, 25, 12, 22, 11, 90]
    print('Unsorted array:', nums)
    solution.bubble_sort(nums)
    print('Sorted array:', nums)