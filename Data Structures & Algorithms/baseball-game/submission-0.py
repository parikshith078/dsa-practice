class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rec = []

        for i in ops:
            if i == "C":
                rec.pop()
            elif i == "D":
                rec.append(rec[-1]*2)
            elif i == "+":
                rec.append(rec[-1] + rec[-2])
            else:
                rec.append(int(i))

        return sum(rec)
        