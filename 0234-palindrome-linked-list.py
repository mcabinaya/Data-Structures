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
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while (slow != None) & (fast != None):
            if fast.next != None:
                slow = slow.next
                fast = fast.next.next
            else:
                break
        revHead = self.reverseList(slow)
        
        curr = head
        revcurr = revHead
        while revcurr != None:
            #print curr.val, revcurr.val
            if curr.val != revcurr.val:
                return False
            curr = curr.next
            revcurr = revcurr.next
        return True
