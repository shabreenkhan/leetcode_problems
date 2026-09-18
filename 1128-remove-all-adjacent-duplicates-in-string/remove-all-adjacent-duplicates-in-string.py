class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in s:
            if not st:
                st.append(i)
            else:
                if i == st[-1]:  # current == previous one  for finding a duplicate adajacent
                    st.pop()
                else:
                    st.append(i)
        return ''.join(st)
    
