class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums_index = {}
        for a_index,a in enumerate(nums):
            b = target - a
            if b in seen_nums_index :
                return [seen_nums_index[b], a_index]
            seen_nums_index[a] = a_index