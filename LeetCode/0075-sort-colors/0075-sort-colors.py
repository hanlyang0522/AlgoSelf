class Solution:
    def sortColors(self, nu: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, mid = 0, 0
        hi = len(nu) - 1

        while mid <= hi:
            if nu[mid] == 0:
                nu[lo], nu[mid] = nu[mid], nu[lo]
                lo, mid = lo + 1, mid + 1
            elif nu[mid] == 1:
                mid += 1
            else:  # 2
                nu[mid], nu[hi] = nu[hi], nu[mid]
                hi -= 1