class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = self.prefixSums(nums)
        total = prefix[-1]
        for i in range(len(nums)):
            if prefix[i] == total - prefix[i+1]:
                return i
        return -1

    def prefixSums(self, nums: List[int]) -> List[int]:
        total=0
        prefix=[0]
        for n in nums:
            total+=n
            prefix.append(total)
        return prefix
