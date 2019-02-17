class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        nums_times=nums.count(val)
        for i in range(nums_times):
            nums.remove(val)    
        return len(nums)
