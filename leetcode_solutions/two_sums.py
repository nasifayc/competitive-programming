class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hash:
                return [i, hash[dif]]
            hash[n] = i
             
        return []
