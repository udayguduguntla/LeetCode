class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=(-1)*(int(str(abs(x))[::-1]))
            return 0 if x < -2 ** 31 else x
        else:
            x=(int(str(abs(x))[::-1]))
            return 0 if x > 2 ** 31 - 1 else x