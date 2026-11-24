class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nb_0 = 0
        nb_1 = 0

        for i in range(len(nums)):
            n = nums[i]
            switched = False
            if n == 0 :
                n = nums[nb_0]
                switched = True 
                nums[nb_0] = 0
                nb_0 += 1
            if n == 1 :
                start_1 = nb_0 + nb_1 -1 if switched else nb_0 + nb_1
                n = nums[start_1]
                nums[start_1] = 1
                nb_1 +=1 if not switched else 0
            if n == 2 :
                nums[i] = 2

            
        



            
