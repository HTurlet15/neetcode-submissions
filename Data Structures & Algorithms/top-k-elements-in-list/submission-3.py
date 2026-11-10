class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for n in nums :
            frequency[n] += 1
        
        appear = [[] for i in range(len(nums))]
        for key in frequency :
            appear[frequency[key]-1].append(key)
        
        max=[]
        for i in range(len(appear)-1,-1,-1):
            if len(appear[i])>0:
                for j in range (len(appear[i])):
                    max.append(appear[i][j])
                    if len(max)==k:
                        return max
                