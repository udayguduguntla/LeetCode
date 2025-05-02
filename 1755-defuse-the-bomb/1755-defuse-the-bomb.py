class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l=[];n=len(code)
        if k>0:
            code=code+code[:k]
            for i in range(n):
                l.append(sum(code[i+1:i+k+1]))
        elif k<0:
            code=code[k:]+code
            for i in range(n):
                l.append(sum(code[i:i-k]))
        else:
            l=[0]*len(code)
        return l