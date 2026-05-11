class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l: 
            mid = (r + l) // 2
            curr = nums[mid] 

            if curr == target:
                return mid
            
            if curr > target:
                r = mid - 1
            else:
                l = mid + 1


        return -1
        