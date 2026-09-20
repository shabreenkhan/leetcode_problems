class Solution:
    def reverseDegree(self, s: str) -> int:
        t=0
        for i ,char in enumerate(s,start=1):
            rev = ord('z') - ord(char)+1

            t += rev * i
        return t