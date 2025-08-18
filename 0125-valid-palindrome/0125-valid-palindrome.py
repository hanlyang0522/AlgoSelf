import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_eng = re.sub("[^a-zA-Z0-9]", "", s)
        s_englower = s_eng.lower()

        return s_englower == s_englower[::-1]