class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]

        for i in nums:
            counter[i] += 1
        
        idx = 0
        for i in range(len(counter)):
            times = counter[i]
            for _ in range(times):
                nums[idx] = i
                idx += 1

