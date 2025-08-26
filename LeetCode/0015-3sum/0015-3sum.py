class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li = []
        x = 0
        nums = sorted(nums)

        while x < len(nums) - 2:
            if x != 0 and nums[x] == nums[x - 1]:
                x += 1
                continue

            target = -nums[x]
            y, z = x + 1, len(nums) - 1

            while y < z:
                if y != x + 1 and nums[y] == nums[y - 1]:
                    y += 1
                    continue
                if z != len(nums) - 1 and nums[z] == nums[z + 1]:
                    z -= 1
                    continue

                if nums[y] + nums[z] == target:
                    li.append([nums[x], nums[y], nums[z]])
                    y += 1
                elif nums[y] + nums[z] < target:
                    y += 1
                else:
                    z -= 1

            x += 1

        return li