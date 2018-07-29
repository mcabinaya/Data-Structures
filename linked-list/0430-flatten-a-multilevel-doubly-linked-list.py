"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        if not head:
            return None
        else:
            tail = self.returnRecursiveTail(head)
            '''
            curr = head
            while curr != None:
                print curr.val
                curr = curr.next
            '''
            return head
        
    def returnRecursiveTail(self, head):
        curr = head
        head_flag = 0
        if (head.next == None) and (head.child != None):
            head_flag = 1
            
        while (curr.next != None) or (head_flag == 1):
            
            if head_flag == 1:
                head_flag = 0
                
            if curr.child != None:
                temp_next = curr.next
                temp_head = curr.child
                curr.child = None
                curr.next = temp_head
                temp_head.prev = curr
                
                tail = self.returnRecursiveTail(temp_head)
                
                tail.next = temp_next
                if temp_next != None:
                    temp_next.prev = tail
                    curr = temp_next
                else:
                    curr = tail
            
            else:
                curr = curr.next
        
        return curr
           
