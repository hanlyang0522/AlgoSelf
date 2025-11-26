class Solution:
    def longestPalindrome(self, s: str) -> int:        
        di = defaultdict(int)

        for l in s:
            di[l] += 1

        num = 0
        flag = False

        for k, v in di.items():
            if v % 2 == 0:
                num += v
            else:
                num += v - 1

                if not flag:
                    num += 1
                    flag = True

        return num