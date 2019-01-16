class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.append(i)
                nums.remove(i)
        print(nums)
       """
        另一种方法
        append_times=nums.count(0)
        for i in range(append_times):
            nums.remove(0)
            nums.append(0)     
        print(nums)
       """
