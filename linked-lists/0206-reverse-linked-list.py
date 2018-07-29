# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            tail = head
            temp = None
            while tail.next != None:
                temp = tail.next
                tail.next = tail.next.next
                temp.next = head
                head = temp
            return head

