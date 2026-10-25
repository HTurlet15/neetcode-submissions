class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appears = {}
        for i in nums :
            if i not in appears :
                appears[i] = True
            else :
                return True
        return False