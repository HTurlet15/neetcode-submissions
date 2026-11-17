class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chain = defaultdict(int)
        len_max = 0
        for val in nums :
            if val in chain:
                continue
            chain[val] = chain.get(val-1, 0) + 1 + chain.get(val+1, 0)
            first_val = val - chain.get(val-1, 0)
            end_val = val + chain.get(val+1, 0)
            chain[first_val] = chain[val]
            chain[end_val] = chain[val]
            if chain[val] > len_max :
                len_max = chain[val]
        return len_max