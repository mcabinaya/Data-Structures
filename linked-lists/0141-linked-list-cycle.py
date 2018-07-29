# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        if (curr == None) or (curr.next == None):
            return False
        else:
            pt1 = curr
            pt2 = curr
            while (pt1 != None) & (pt2 != None):    
                if pt2.next != None:
                    pt1 = pt1.next
                    pt2 = pt2.next.next
                    if pt2 == pt1:
                        return True
                
                else:
                    break
            return False

        
