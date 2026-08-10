class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro=1
        sum_=0
        while n!=0:
            r=n%10
            pro=pro*r
            sum_=sum_+r
            n=n//10
        difference=pro-sum_
        return difference