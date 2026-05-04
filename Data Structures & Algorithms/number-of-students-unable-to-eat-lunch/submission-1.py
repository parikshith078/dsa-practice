
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        smap = {0: 0, 1: 0}
        for s in students:
            smap[s] += 1
        
        servedCount = 0
        sandwichCount = len(sandwiches)
        for i in sandwiches:
            if smap[i] > 0:
                smap[i] -= 1
                servedCount += 1
            else:
                return sandwichCount - servedCount 
        
        return 0