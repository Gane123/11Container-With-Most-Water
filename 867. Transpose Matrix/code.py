class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        第二种方法
        return [[row[col] for row in A] for col in range(len(A[0]))]
        """
        return list(map(list,zip(*A)))
