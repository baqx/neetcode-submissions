class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        noOfNums = len(nums)
        k = noOfNums - nums.count(val)

        remaining = [num for num in nums if num!=val]
        
        for i in range(len(remaining)):
            nums[i] = remaining[i]

        return k