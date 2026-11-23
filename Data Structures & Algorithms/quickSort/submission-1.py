# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.pairs = pairs
        self.sort(0,len(pairs)-1)
        return pairs

    def sort(self,start,end):
        if end-start<=0:
            return 

        pivot = self.pairs[end]
        i_less = start
        for i in range(start,end) :
            p = self.pairs[i]
            if p.key < pivot.key:
                self.pairs[i], self.pairs[i_less] = self.pairs[i_less], self.pairs[i]
                i_less +=1
        self.pairs[i_less], self.pairs[end] = self.pairs[end], self.pairs[i_less]

        self.sort(start,i_less-1)
        self.sort(i_less+1,end)