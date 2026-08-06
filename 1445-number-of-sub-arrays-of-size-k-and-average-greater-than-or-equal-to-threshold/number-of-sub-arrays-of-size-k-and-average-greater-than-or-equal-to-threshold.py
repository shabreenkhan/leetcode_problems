class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left=0
        currentsum_=0
        for right in range(len(arr)):
            currentsum_ += arr[right]
            if right >= k-1:
                avg = currentsum_ // k
                if avg >= threshold:
                    count+=1
                currentsum_ -= arr[left]
                left+=1
        return count
