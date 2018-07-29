class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = 0
        i1 = 0
        m2 = 0
        for i, val in enumerate(nums):
            #print("----")
            #print(i,val)
            if val > m1:
                m2 = m1
                m1 = val
                i1 = i
            if (val < m1) & (val > m2):
                #print(i,val)
                m2 = val
            #print(m1)
            #print(m2)
        
        if m2 <= (m1/2):
            return i1
        else:
            return -1
            

        
