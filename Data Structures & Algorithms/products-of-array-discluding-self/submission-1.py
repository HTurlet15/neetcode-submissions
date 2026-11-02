class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.prefix(nums)
        suffix = 1
        output = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1) :
            output[i] = prefix[i] * suffix
            suffix = suffix*nums[i]
        return output
        
    def prefix(self, nums: List[int]) -> List[int]:
        prefix = [1]
        total = 1
        for i in range(len(nums)-1) :
            total = total*nums[i]
            prefix.append(total)
        return prefix
