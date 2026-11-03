class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        prefixSum = {0 : 1}
        count = 0
        for i in range(len(nums)):
            total+=nums[i]
            prefix.append(total)
            if (prefix[i] - k) in prefixSum:
                count+=prefixSum[prefix[i]-k]
            prefixSum[prefix[i]] = 1 + prefixSum.get(prefix[i],0)

        return count