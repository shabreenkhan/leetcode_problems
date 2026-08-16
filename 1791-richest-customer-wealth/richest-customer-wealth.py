class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            w=sum(i)
            if w>m:
                m=w
        return m
