class Solution:
    def matrixReshape(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
        from functools import reduce
        all_nums=reduce(lambda x,y:x+y,nums)
        if r*c>len(nums)*len(nums[0]):
            return nums
        return [all_nums[i:i+c] for i in range(0, len(all_nums), c)]
