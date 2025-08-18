class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_englower = "".join([char for char in s if char.isalnum()]).lower()

        return s_englower == s_englower[::-1]