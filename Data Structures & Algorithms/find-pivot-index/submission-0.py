class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = self.prefixSums(nums)
        postfix = self.postfixSums(nums)
        length = len(nums)

        for i in range(length):
            if prefix[i] == postfix[length-i-1]:
                return i
        return -1

    def prefixSums(self, nums: List[int]) -> List[int]:
        total=0
        prefix=[0]
        for n in nums:
            total+=n
            prefix.append(total)
        return prefix

    def postfixSums(self, nums: List[int]) -> List[int]:
        total=0
        postfix=[0]
        for i in range(len(nums)-1,-1,-1):
            total+=nums[i]
            postfix.append(total)
        return postfix
