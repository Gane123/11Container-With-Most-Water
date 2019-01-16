class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        return True if len(set(nums)) < len(nums) else False   %另一种方法
        """
        A=set(nums)     %set()：集合，元素唯一，无序
        if len(A)<len(nums):
            return True
        else:
            return False
