class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    
        temp_nums = list(range(0, len(nums)+1))
        for temp_num in temp_nums:
            if temp_num not in nums:
                return temp_num