class Solution:
    def isValid(self, s: str) -> bool:
        li = ["0"] * 10000
        idx = 0

        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                li[idx] = s[i]
                idx += 1
            else:
                if s[i] == ")" and li[idx - 1] != "(":
                    return False
                elif s[i] == "]" and li[idx - 1] != "[":
                    return False
                elif s[i] == "}" and li[idx - 1] != "{":
                    return False

                idx -= 1

        if idx == 0:
            return True
        else:
            return False