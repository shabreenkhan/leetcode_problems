class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=sorted(nums1+nums2)
        b=len(a)
        if b%2==1:
           return a[b//2]
        else:  
             return (a[b//2-1]+a[b//2])/2