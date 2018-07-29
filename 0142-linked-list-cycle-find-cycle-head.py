# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        if (curr == None) or (curr.next == None):
            return None
        else:
            slow = curr
            fast = curr
            cycle_flag = 0
            while (slow!= None) & (fast != None):
                if (fast.next != None):                
                    slow = slow.next
                    fast = fast.next.next
                    if slow == fast:
                        cycle_flag = 1
                        break
                else:
                    break
            if cycle_flag == 0:
                return None
            else:
                new = head
                while(new != fast):
                    new = new.next
                    fast = fast.next
                return fast
            
