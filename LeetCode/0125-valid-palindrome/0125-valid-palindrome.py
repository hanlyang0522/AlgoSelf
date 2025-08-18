import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_eng = re.sub("[^a-zA-Z0-9]", "", s)
        s_englower = s_eng.lower()

        for i in range(len(s_englower)//2):
            if s_englower[i] != s_englower[-1 - i]:
                return False

        return True