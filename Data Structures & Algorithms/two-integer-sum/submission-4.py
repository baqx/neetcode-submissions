class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total_nums=len(nums)
        i = 0
        j = total_nums-1

        while i < total_nums:
            j = total_nums-1
            while j < total_nums and j >= 0:

                if i == j:
                    j -= 1
                    continue 
                sum_of_nums = nums[i] + nums[j]
                if sum_of_nums == target:
                    return [i,j]
                j -= 1
            i += 1
            j = 0

