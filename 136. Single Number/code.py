class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        return 2 * sum(set(nums)) - sum(nums) %第二种方法
        """
        nums1=[]
        for i in nums:
            if i not in nums1:
                nums1.append(i)
            else:
                nums1.remove(i)
        return nums1.pop()
