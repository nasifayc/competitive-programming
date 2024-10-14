import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        while k > 1:
            heapq.heappop(max_heap)
            k -= 1

        return -max_heap[0]
        