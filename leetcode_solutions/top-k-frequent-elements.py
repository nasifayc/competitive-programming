import heapq
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        hashtable = Counter(nums)
        value_pairs = [(-v,k) for k,v in hashtable.items()]
        heapq.heapify(value_pairs)

        i = 0
        res = []
        while i < k:
           val = heapq.heappop(value_pairs)
           res.append(val[1])
           i += 1
        return res

