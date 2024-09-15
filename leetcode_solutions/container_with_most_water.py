from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        height.sort()
        print(height)
        # i = len(height)-1

        # while i > 0:
        #     if height[i] < height[i-1]:
        #         return height[i-1] ** 2
        #     else:
        #         i -= 1
        
        # return height[i] ** 2


if __name__ == '__main__':
    solution = Solution()
    solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
   