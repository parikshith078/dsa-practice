class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = ["(", "[", "{"]
        closed = [")", "]", "}"]

        for i in s:
            if i in opened:
                idx = opened.index(i)
                stack.append(idx)
            else:
                if len(stack) == 0:
                    return False

                topIdx = stack.pop()
                if topIdx != closed.index(i):
                    return False
            
        return True if len(stack) == 0 else False
                
        