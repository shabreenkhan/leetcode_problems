class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[]
        a=set(nums1)
        b=set(nums2)
        ans.append(list(a.difference(b)))
        ans.append(list(b.difference(a)))
        return list(ans)