class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for to in tokens:

            if to in ["+", "-", "*", "/"]:
                n2, n1 = st.pop(), st.pop()
                n3 = str(int(eval(n1 + to + n2)))
                st.append(n3)

            else:
                st.append(to)

        return int(st[0])