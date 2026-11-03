class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        for val in nums:
            total+=val
            prefix.append(total)
    
        prefixSum = {0 : 1}
        count = 0
        for i in range(len(nums)):
            if (prefix[i] - k) in prefixSum:
                count+=prefixSum[prefix[i]-k]
            prefixSum[prefix[i]] = 1 + prefixSum.get(prefix[i],0)

        return count