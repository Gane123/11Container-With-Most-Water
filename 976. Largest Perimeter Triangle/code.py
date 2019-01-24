class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse = True)
        for i in range(len(A)):
            for j in range(i+2,(len(A))):
                if A[j]+A[i+1]>A[i]:
                    return A[i]+A[i+1]+A[j]
        return 0
