class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx=0
        count=1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count+=1
                i+=1
            else:
                mx=max(mx,count)
                count=1
        return max(mx,count)