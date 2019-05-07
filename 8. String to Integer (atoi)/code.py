class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.strip()
        if len(str)==0:
            return 0
        temp="0"
        result=0
        i=0
        if str[0] in "+-":
            temp=str[0]
            i=1
        for i in range(i,len(str)):
            if str[i].isdigit():
                temp += str[i]
            else:
                break
        if len(temp)>1:
            result=int(temp)
        MAX_INT=2147483647
        MIN_INT=-2147483648
        if result>MAX_INT:
            return MAX_INT
        if result<MIN_INT:
            return MIN_INT
        else:
            return result
