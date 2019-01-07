class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        number=int(input(''))
        height=[int(n) for n in number.split()]
          height=[random.randint(1,20) for a in range(10)]
        """
    
        S_array=[]
        for i in height:
            if i<height[-1]:
                s=i*(len(height)-height.index(i)-1)
                S_array.append(s)
            else:
                s=height[-1]*(len(height)-height.index(i)-1)
                S_array.append(s)
        print(max(S_array))
