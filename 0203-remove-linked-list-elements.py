# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """ 
        if head == None:
            return None
        if (head.next == None) & (head.val == val):
            return None
        while (head.val == val) & (head.next != None):
            head = head.next
        prev = head
        curr = head.next
        if curr != None:
            while (curr.next != None):
                if curr.val == val:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    curr = curr.next
                    prev = prev.next
            if curr.val == val:
                prev.next = None
        if (head.val == val) & (head.next == None):
            return None
        return head
            
