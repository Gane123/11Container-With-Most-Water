class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0 or N==1 :
            return N
        else:
            return self.fib(N-1)+self.fib(N-2)
        """
        第二种写法
         return N if N==0 or N==1 else self.fib(N-1)+self.fib(N-2)
        """
