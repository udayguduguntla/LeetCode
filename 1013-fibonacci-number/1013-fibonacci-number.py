class Solution:
    def fib(self, n: int) -> int:
        if n<2:
          return n
        else:
            a=0
            b=1
            for i in range(1,n+1):
                a,b=b,a+b
            return a
        