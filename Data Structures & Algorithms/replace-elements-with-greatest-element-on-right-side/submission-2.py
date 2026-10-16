class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        max_right_list = []
        arr.reverse()
        for i in range(1,len(arr)) :
            if arr[i-1] > max_right :
                max_right = arr[i-1]
            max_right_list.append(max_right)
        max_right_list.reverse()
        max_right_list.append(-1)
        return max_right_list