class Solution:
    def checkDivisibleNumber(self, n: int) -> bool:
        digits = list(map(int,set(str(n))))
        if 0 in digits:
            return False
        return sum(1 for i in digits if n%i == 0) == len(digits)

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # approach - 1

        # nums = [i for i in range(left,right+1) if self.checkDivisibleNumber(i)]
        # return nums

        # approach - 2

        nums = []
        for i in range(left,right+1):
            if'0' not in str(i):
                num = i
                remind = 0
                while num > 0 and remind == 0:
                    digit = num % 10
                    num = num // 10
                    remind = i % digit
                if remind == 0:  nums.append(i)
        return nums