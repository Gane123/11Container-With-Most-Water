class Solution:
    def reverse(self, x: int) -> int:
        a=x<0
        if a:
            b=int('-'+str(-x)[::-1])
        else:
            b=int(str(x)[::-1])

        if b> 2**31 or b< -2**31-1:
            return 0
        return b
