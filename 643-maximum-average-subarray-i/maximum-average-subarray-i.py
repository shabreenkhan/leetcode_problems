class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Brute force solution - fails due to len(n) can be as long as 10^5
        #Generate all sub-arrays and keep the averages of those whose length is k
        mxavg = -10000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum += nums[right]
            if right >= k-1:
                avg = currentsum / k
                mxavg=max(avg,mxavg)
                #substring the value on left (window size is exceed k)
                currentsum -= nums[left]
                left += 1
        return mxavg    
                        