class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        
        for i in range(len(nums)):
            if target - nums[i] in di:
                return [di[target - nums[i]], i]

            di[nums[i]] = i