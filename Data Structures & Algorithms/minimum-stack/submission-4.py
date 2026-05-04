class MinStack:

    def __init__(self):
        self.stack = []
        self.mStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cMin = min(val, self.mStack[-1] if len(self.mStack) else val)
        self.mStack.append(cMin)

    def pop(self) -> None:
        self.stack.pop()
        self.mStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mStack[-1]
        
