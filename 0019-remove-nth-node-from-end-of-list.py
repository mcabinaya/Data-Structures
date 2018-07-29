# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pt1 = head
        pt2 = head 
        count = 0
        prev = None
        while pt1.next != None:
            count += 1
            if count < n:
                pt1 = pt1.next
            else:
                pt1 = pt1.next
                prev = pt2
                pt2 = pt2.next
        if count == 0:
            return None
        else:
            if prev == None:
                return pt2.next
            else:
                prev.next = pt2.next
                pt2.next = None
                return head
