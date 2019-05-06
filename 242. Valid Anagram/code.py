class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        '''return "".join((lambda x:(x.sort(),x)[1])(list(s)))=="".join((lambda x:(x.sort(),x)[1])(list(t)))'''
