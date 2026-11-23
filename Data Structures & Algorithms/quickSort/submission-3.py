# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs,0,len(pairs)-1)
        return pairs

    def sort(self,pairs,start,end):
        if end-start<=0:
            return 

        pivot = pairs[end]
        i_less = start
        for i in range(start,end) :
            p = pairs[i]
            if p.key < pivot.key:
                pairs[i], pairs[i_less] = pairs[i_less], pairs[i]
                i_less +=1
        pairs[i_less], pairs[end] = pairs[end], pairs[i_less]

        self.sort(pairs,start,i_less-1)
        self.sort(pairs,i_less+1,end)