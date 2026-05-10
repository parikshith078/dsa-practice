class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSort(points, 0, len(points) - 1)
        return points[:k]
    
    def quickSort(self, points: List[List[int]], s: int, e: int):
        if (e - s + 1) <= 1:
            return 
        pscore = self.score(points[e])
        left = s

        for i in range(s, e):
            score = self.score(points[i])
            if score <= pscore:
                tmp = points[i]
                points[i] = points[left]
                points[left] = tmp
                left += 1
        
        # final pivot swap
        tmp = points[e]
        points[e] = points[left]
        points[left] = tmp

        self.quickSort(points, s, left - 1)
        self.quickSort(points, left + 1, e)
        
    def score(self, point: List[int]) -> float:
        x, y = point
        return math.sqrt(x**2 + y**2)
        