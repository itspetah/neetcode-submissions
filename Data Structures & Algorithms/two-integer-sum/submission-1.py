class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        calculations = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in calculations:
                return [calculations[complement], i]
            else:
                calculations[num] = i