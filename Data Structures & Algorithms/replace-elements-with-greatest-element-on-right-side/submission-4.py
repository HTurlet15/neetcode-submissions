class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for i in range(len(arr)-1,-1,-1) :
            old_arr_value = arr[i]
            arr[i] = max_right
            if old_arr_value > max_right :
                max_right = old_arr_value
        return arr