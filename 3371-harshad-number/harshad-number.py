class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_=0
        temp = x
        while x!=0:
            r=x%10
            sum_ += r
            x=x//10
        if temp % sum_ == 0:
            return sum_
        else:
            return -1

        