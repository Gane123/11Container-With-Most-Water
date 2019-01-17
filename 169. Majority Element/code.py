class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,temp=0,0
        for num in nums:
            if count == 0:
                temp = num
            if num != temp:
                count -= 1
            else:
                count += 1
        return temp
