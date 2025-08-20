class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1, c2 = Counter(ransomNote), Counter(magazine)

        for ch in c1.keys():
            if c2[ch] < c1[ch]:
                return False

        return True