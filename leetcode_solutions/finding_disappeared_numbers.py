
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] -1
            if correct < len(nums) and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result

    


