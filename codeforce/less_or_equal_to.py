from typing import List

class Solution:
    def sortArray(self, nums: List[int], n: int, k: int) -> int:
        # Sort the array
        nums.sort()

        if k == 0:
            # If we need 0 elements <= x, we need a value less than the smallest element
            if nums[0] > 1:
                return 1
            else:
                return -1
        else:
            # We need exactly k elements <= x
            if k == n or nums[k - 1] < nums[k]:
                return nums[k - 1]
            else:
                return -1

# Example usage:
if __name__ == '__main__':
    solution = Solution()
    nums = [3, 7, 5, 1, 10, 3, 20]
    n = len(nums)
    k = 2
    print(solution.sortArray(nums, n, k))  # Expected Output: 3
