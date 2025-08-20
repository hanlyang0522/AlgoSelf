class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1, c2 = Counter(ransomNote), Counter(magazine)

        return (c1 & c2) == c1
