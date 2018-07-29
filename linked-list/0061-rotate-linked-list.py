# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
        else:
            flag = 0
            temp_count =0
            new_k = 0
            while True:
                if flag == 0:
                    count = 0
                present_head = head
                curr = head
                prev = None

                while curr.next != None:
                    if flag == 0:
                        count += 1
                    prev = curr
                    curr = curr.next

                if flag == 0:
                    list_len = count+1
                    new_k = k % list_len
                    flag = 1

                if (temp_count < new_k):
                    temp_count += 1
                    curr.next = present_head
                    if prev != None:
                        prev.next = None
                    head = curr
                else:
                    break
            return head
            
            
            
