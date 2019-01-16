class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        第二种方法
        return [i for i in A if i & 1 ==0]+[i for i in A if i & 1 ==1]
        """
        idx=0
        for i in range(len(A)):
            if A[i] & 1==0:
                A[i],A[idx]=A[idx],A[i]
                idx+=1
        return A
