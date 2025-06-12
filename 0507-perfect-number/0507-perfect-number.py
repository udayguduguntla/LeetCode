class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:  return False
        s=1
        i=2
        while i*i <= num:
            if num % i == 0:
                s += i
                if i != num//2:
                    s += (num//i)
            i += 1
        return num == s