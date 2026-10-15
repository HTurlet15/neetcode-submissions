class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for nums_value in nums:
            if val!=nums_value:
                nums[k] = nums_value
                k+=1
        return k
        
