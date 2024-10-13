from typing import List


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        heap = []
        for num in stones:
            heapq.heappush(heap, -num)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y > x:
                heapq.heappush(heap, -(y-x))
            
            else:
                break

        return -heap[0] if heap else 0

        

        