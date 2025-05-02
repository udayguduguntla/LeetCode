class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        p=1
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                c=2
                for k in range(j+1,len(points)):
                    x3,y3=points[k]
                    c+= ((x2-x1)*(y3-y1) == (x3-x1)*(y2-y1))
                p=max(p,c)
        return p