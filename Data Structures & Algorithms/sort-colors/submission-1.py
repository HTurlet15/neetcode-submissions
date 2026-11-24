class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3
        for n in nums :
            count[n]+=1
        
        n0 = count[0]
        n1 = count[1]
        n2 = count[2]
        n_i = 0
        n = 0
        for i in range(len(nums)):
            if n_i == count[n]:
                n += 1
                n_i = 0
            if n_i < count[n]:
                nums[i] = n
            n_i += 1
            if n_i == count[n]:
                n += 1
                n_i = 0


            
