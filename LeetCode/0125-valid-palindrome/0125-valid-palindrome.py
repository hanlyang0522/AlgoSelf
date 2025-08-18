import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_englower = "".join([char for char in s if char.isalnum()]).lower()

        for i in range(len(s_englower)//2):
            if s_englower[i] != s_englower[-1 - i]:
                return False

        return True