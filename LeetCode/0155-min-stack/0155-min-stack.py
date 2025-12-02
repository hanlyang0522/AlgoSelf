from collections import deque


class MinStack:
    dq = deque()

    def __init__(self):
        self.dq.clear()

    def push(self, val: int) -> None:
        self.dq.append(val)

    def pop(self) -> None:
        self.dq.pop()

    def top(self) -> int:
        return self.dq[-1]

    def getMin(self) -> int:
        li = list(self.dq)
        
        return min(li)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
