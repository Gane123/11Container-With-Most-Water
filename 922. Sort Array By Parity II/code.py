from itertools import chain
class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        A1=[]
        A2=[]
        for i in A:
            if i & 1:
                A1.append(i)
            else:
                A2.append(i)
        return list(chain(*zip(A2,A1)))
