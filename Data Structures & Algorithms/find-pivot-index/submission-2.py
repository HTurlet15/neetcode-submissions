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
        for i in range(len(nums)):
            total+=nums[i]
            nums[i] = total
        return [0] + nums
