class Solution:
    def countCommas(self, n: int) -> int:
        t=0
        thresh=1000
        while n>=thresh:
            t+=(n-thresh+1)
            thresh*=1000
        return t