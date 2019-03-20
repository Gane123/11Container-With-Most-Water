class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s=collections.Counter(s)
        index=0
        for i in s:
            if count_s[i]==1:
                return index
            else:
                index+=1
        return -1
