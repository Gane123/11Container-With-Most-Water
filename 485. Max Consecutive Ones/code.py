class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int':
        j=0
        m=0
        for i in nums:
            if i==1:
                j+=1
                m=max(m,j)
            else: 
                j=0
        return m
