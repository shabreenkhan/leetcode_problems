class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result_set=set()
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_ > 0:
                    right-=1
                elif sum_ < 0:
                    left+=1
                else:
                    result_set.add(tuple([nums[i],nums[left],nums[right]]))
                    left+=1   #we want to find more indices so we don't return it
                    right-=1
        return list(result_set)
