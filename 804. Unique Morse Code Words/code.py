class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=[]
        for word in words:
            s=""
            for i in range(len(word)):
                s+=a[ord(word[i])-ord('a')]
            result.append(s)
        return  len(set(result)) 
