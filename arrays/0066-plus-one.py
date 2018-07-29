class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output = digits[:]
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i]+1
            if temp == 10:
                output[i] = 0
            else:
                output[i] = temp
                carry = 0
                break
        if output[0] == 0:
            output.insert(0,1)
        return output
            
        
