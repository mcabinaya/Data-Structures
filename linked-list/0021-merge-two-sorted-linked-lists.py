# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None) & (l2 == None):
            return None
        elif (l1 != None) & (l2 == None):
            return l1
        elif (l1 == None) & (l2 != None):
            return l2
        else:            
            pt1 = l1
            pt2 = l2
            curr = None
            head = l1
            while pt1 != None:
                start = pt2
                count = 0
                prev = None
                while (pt2 != None):
                    if (pt2.val <= pt1.val):
                        count += 1
                        prev = pt2
                        pt2 = pt2.next
                    else:
                        break    
                end = prev
                if count != 0:
                    if curr == None:
                        head = start
                        end.next = pt1
                    else:
                        curr.next = start
                        end.next = pt1
                    curr = pt1
                    pt1 = pt1.next
                else:
                    if curr == None:
                        head = pt1
                    curr = pt1
                    pt1 = pt1.next
            if pt2 != None:
                curr.next = pt2
            return headß    
