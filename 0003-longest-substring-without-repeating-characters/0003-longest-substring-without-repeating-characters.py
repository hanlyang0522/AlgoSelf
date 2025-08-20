class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0
        left = 0
        letter_pos = {}

        for right, c in enumerate(s):
            if c in letter_pos and left <= letter_pos[c]:
                left = letter_pos[c] + 1  # 같은 문자까지 잘라냄 -> 시작위치는 그 다음

            maxL = max(maxL, right - left + 1)
            letter_pos[c] = right

        return maxL