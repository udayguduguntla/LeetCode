class Solution:
    def checkDivisibleNumber(self, n: int) -> bool:
        digits = list(map(int,set(str(n))))
        if 0 in digits:
            return False
        return sum(1 for i in digits if n%i == 0) == len(digits)

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = [i for i in range(left,right+1) if self.checkDivisibleNumber(i)]
        return nums