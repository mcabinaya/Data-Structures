# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
       
        tojoin = self.swapPairs(head.next.next)
        
        temp = head.next
        head.next = tojoin
        temp.next = head
        return temp
        
