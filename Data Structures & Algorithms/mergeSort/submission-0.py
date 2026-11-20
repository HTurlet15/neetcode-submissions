# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        if n<=1:
            return pairs

        m=n//2
        sub_1 = self.mergeSort(pairs[:m])
        sub_2 = self.mergeSort(pairs[m:])

        i1 = 0
        i2 = 0
        i = 0

        while i < n :
            if i1 == len(sub_1):
                pairs[i] = sub_2[i2]
                i2 += 1
                i+=1
                continue
            if i2 == len(sub_2):
                pairs[i] = sub_1[i1]
                i1 += 1
                i+=1
                continue
            
            if sub_1[i1].key <= sub_2[i2].key:
                pairs[i] = sub_1[i1]
                i1 += 1
                i+=1
            else :
                pairs[i] = sub_2[i2]
                i2 += 1
                i+=1
        return pairs

