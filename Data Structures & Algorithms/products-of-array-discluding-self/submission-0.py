class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.prefix(nums)
        suffix = self.suffix(nums)
        output = [prefix[i]*suffix[i] for i in range(len(prefix))]
        return output
        
    def prefix(self, nums: List[int]) -> List[int]:
        prefix = [1]
        total = 1
        for i in range(len(nums)-1) :
            total = total*nums[i]
            prefix.append(total)
        return prefix
    
    def suffix(self, nums: List[int]) -> List[int]:
        suffix = [1]*len(nums)
        total = 1
        for i in range(len(nums)-2,-1,-1) :
            total = total*nums[i+1]
            suffix[i] = total
        return suffix
