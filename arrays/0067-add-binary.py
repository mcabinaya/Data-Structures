class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a != len_b:
            if len_a < len_b:
                a = ("0"*(len_b-len_a))+a
            else:
                b = ("0"*(len_a-len_b))+b
        #print a, b
        
        result = ""
        carry = 0
        for i in range(len(a)-1, -1, -1):
            num1 = int(a[i])
            num2 = int(b[i])         
            if num1 + num2 + carry == 0:
                ans = 0
                carry = 0
            elif num1 + num2 + carry == 1:
                ans = 1
                carry = 0
            elif num1 + num2 + carry == 2:
                ans = 0
                carry = 1  
            elif num1 + num2 + carry == 3:
                ans = 1
                carry = 1    
            #print ans, carry
            result = str(ans) + result
        
        if carry == 1: result = "1" + result
        return result
                
        
            
            
            
        
