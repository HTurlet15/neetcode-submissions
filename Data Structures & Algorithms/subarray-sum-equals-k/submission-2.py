class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:      
        count = 0
        total = 0
        prefix = []
        seen_prefixes = {0 : 1}
        for i in range(len(nums)):
            total+=nums[i]
            prefix.append(total)
            if prefix[i] - k in seen_prefixes:
                count += seen_prefixes[prefix[i]-k]
            seen_prefixes[prefix[i]] = 1 + seen_prefixes.get(prefix[i],0)
        return count
            
                


