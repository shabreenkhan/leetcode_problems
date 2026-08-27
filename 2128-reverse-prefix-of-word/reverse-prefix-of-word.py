class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_l=list(word)
        s=[]
        found=False
        for i in range(len(word_l)):
            s.append(word_l[i])
            if word_l[i] == ch:
                found=True
                break
        if not found:
            return word
        rev=s[::-1]
        r=[]
        for j in range(i+1,len(word_l)):
            r.append(word_l[j])
        return "".join(rev+r)
                



        