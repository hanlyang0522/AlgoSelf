class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        num0, num1, num2 = 0, 0, 0

        for i in nums:
            if i == 0:
                num0 += 1
            elif i == 1:
                num1 += 1
            else:
                num2 += 1

        idx = 0

        while num0 > 0:
            nums[idx] = 0
            idx += 1
            num0 -= 1

        while num1 > 0:
            nums[idx] = 1
            idx += 1
            num1 -= 1

        while num2 > 0:
            nums[idx] = 2
            idx += 1
            num2 -= 1