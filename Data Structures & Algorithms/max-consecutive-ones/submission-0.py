class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        rMax = 0
        gMax = 0

        for i in nums:
            if i == 1:
                rMax += 1
            else:
                gMax = max(rMax, gMax)
                rMax = 0
            
        return max(rMax, gMax)
        