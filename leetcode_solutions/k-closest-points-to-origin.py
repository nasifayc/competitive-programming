import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(min_heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res
        