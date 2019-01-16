class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        B=len(nums)
        for i in range(1,k+1):
            nums.insert(0,nums[-i])
        for j in range(1,k+1):
            nums.pop(B)
        print(nums)
