class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        begin = set(nums)
        len_max = 0
        for val in nums :
            if val-1 not in begin:
                length = 1
                while val+1 in begin:
                    length+=1
                    val+=1
                len_max = max(len_max,length)
        return len_max