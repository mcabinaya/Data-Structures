class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {"(":")", "{":"}", "[":"]"}
        mystack = []
        
        for b in s:
            if b in mydict:
                mystack.append(mydict[b])
            else:
                if len(mystack) > 0:
                    temp = mystack.pop()
                    if temp != b:
                        return False
                else:
                    return False
                
        if len(mystack) == 0:
            return True
        else:
            return False
