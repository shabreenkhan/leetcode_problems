def vow(v):
    return v in "aeiouAEIOU"
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left,right=0,len(s)-1
        while left<right:
            if vow(s[left]) and vow(s[right]):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif vow(s[left]):
                right-=1
            elif vow(s[right]):
                left+=1
            else:
                left+=1
                right-=1 
        return "".join(s)