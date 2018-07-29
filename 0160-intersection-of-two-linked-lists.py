# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        currA = headA
        currB = headB
        while (currA != None) or (currB != None): 
            if currA != None:
                lenA += 1
                currA = currA.next
            if currB != None:
                lenB += 1
                currB = currB.next
        offset = abs(lenA - lenB)
        currA = headA
        currB = headB
        if lenA > lenB:
            for i in range(offset):
                currA = currA.next
        else:
            for i in range(offset):
                currB = currB.next
        while currA != currB:
            currA = currA.next
            currB = currB.next
        return currA
            
