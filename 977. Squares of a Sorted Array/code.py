class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        B=[]
        for i in A:
            j=i*i
            B.append(j)
        return sorted(B) 
