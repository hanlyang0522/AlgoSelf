"""

"""

import sys

f = sys.stdin.readline


def solve():
    s = list(f().split())

    base = s[0]

    for i in range(1, len(s)):
        ans = base
        var = s[i]

        while var[-1] in ["*", "[", "]", "&", ";", ","]:
            if var[-1] == "[":
                ans += "[]"
            elif var[-1] == "*":
                ans += "*"
            elif var[-1] == "&":
                ans += "&"

            var = var[:-1]

        var += ";"

        print(ans, var)


if __name__ == "__main__":
    solve()
