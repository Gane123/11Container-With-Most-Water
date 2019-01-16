class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nu=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    nu.append(i)
                    nums2.remove(j)
                    break
        return nu
