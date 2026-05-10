class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]
        right = nums2
        i, l, r = 0, 0, 0

        while len(right) > r and len(left) > l: 
            if left[l] <= right[r]:
                nums1[i] = left[l] 
                l += 1
            else:
                nums1[i] = right[r]
                r += 1
            
            i += 1
        
        while len(right) > r:
            nums1[i] = right[r]
            i += 1
            r += 1

        while len(left) > l:
            nums1[i] = left[l]
            i += 1
            l += 1

