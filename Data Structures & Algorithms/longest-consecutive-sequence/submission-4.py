class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chain = defaultdict(int)
        len_max = 0
        for val in nums :
            if val in chain:
                continue
            chain[val] = 1
            first_val = val
            end_val = val
            if val-1 in chain :
                #val is never seen before and one value is smaller, so val is the new max end
                #of that bottom sequence
                first_val = val - chain[val-1]
                chain[val] += chain[val-1]
            if val+1 in chain :
                #val is never seen before and one value is greater, so val is the new min end
                #of that top sequence
                end_val = val + chain[val+1]
                chain[val] += chain[val+1]
            chain[first_val] = chain[val]
            chain[end_val] = chain[val]
            if chain[val] > len_max :
                len_max = chain[val]
        return len_max