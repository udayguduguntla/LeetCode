class Solution:
    def minGroups(self, it: List[List[int]]) -> int:
        s=[];m=1;c=0
        for i in it:
            a=i[0];b=i[1]
            s.extend([[a,1],[b+1,-1]])
        s=sorted(s,key=lambda x:(x[0],x[1]))
        for i in s:
            if i[1]==1:
                c+=1;print(i,c)
            elif i[1]==-1:
                m=max(m,c);c-=1;print(i,c,m)
        return m