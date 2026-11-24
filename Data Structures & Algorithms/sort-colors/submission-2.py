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
        added_n = 0
        n = 0

        for i in range(len(nums)):
            if added_n < count[n]:
                nums[i] = n

            if added_n == count[n]:
                n += 1
                while count[n] == 0 :
                    n += 1
                added_n = 0
                nums[i] = n
            added_n += 1


            
