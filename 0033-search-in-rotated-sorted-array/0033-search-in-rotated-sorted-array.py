class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            idx = nums.index(target)
        except:
            idx = -1

        return idx