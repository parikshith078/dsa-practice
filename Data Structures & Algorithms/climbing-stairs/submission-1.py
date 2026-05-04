class Solution:
    def __init__(self):
        self.dp = {}

    def climbStairs(self, n: int) -> int:
        return self._ways(n, 0)
    
    def _ways(self, n: int, currStep: int) -> int:
        key = (n, currStep)
        if key in self.dp:
            return self.dp[key]

        if currStep == n:
            return 1
        elif currStep > n:
            return 0
        
        res = self._ways(n, currStep+1) + self._ways(n, currStep+2)
        self.dp[key] = res
        return res
        


        