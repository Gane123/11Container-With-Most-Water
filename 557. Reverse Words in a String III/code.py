class Solution:
    def reverseWords(self, s: str) -> str:
        s1=''
        for i in s.split():
            s2=i[::-1]
            s1+=' '+s2
        return s1[1:]
