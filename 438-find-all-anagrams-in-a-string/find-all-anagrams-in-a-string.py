class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        #step -1 : compute the frequencies of string p
        for i in p:
            d1[i]=d1.get(i,0)+1
        # step - 2: do a k-length sliding window on s
        #count the frequencies of characters in substring into d2
        k=len(p)
        d2={}
        left = 0
        ans = []
        for right in range(len(s)):
            d2[s[right]] = d2.get(s[right],0)+1 #counting freq of substring K
            if right >= k-1:# checking the validity of window
                if d1 == d2:# comparsing hashmap tp check anagrams
                    ans.append(left) # if anangrams adding start index to ans
            #removing the outgoing element-left
                d2[s[left]]-=1
                if d2[s[left]]==0:
                    d2.pop(s[left])
                left+=1
        return ans

