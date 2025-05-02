class Solution:
    def evalRPN(self, t: List[str]) -> int:
        s=[]
        for i in t:
            match i:
                case '+':   a=s.pop()+s.pop();s.append(a)
                case '-':   a=s[-2]-s[-1];s=s[:-2];s.append(a)
                case '*':   a=s.pop()*s.pop();s.append(a)
                case '/':   a=int(s[-2]/s[-1]);s=s[:-2];s.append(a)
                case _: s.append(int(i))
        return s.pop()