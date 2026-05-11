class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        if row == -1:
            return False
        
        return self.bsearch(matrix[row], target)
    
    def bsearch(self, arr: List[int], target: int) -> bool:
        l, r = 0, len(arr) - 1

        while r >= l:
            mid = (r + l) // 2

            if arr[mid] == target:
                return True
            
            if arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
                

    
    def findRow(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while r >= l:
            mid = (r + l) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
        
        return -1

        