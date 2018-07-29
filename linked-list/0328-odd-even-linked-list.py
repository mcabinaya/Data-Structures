# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head
        else:
            oddEnd = head
            evenBegin = head.next
            curr = head.next
            while curr != None:
                if curr.next != None:
                    #print "---"
                    temp = curr.next
                    curr.next = temp.next
                    oddEnd.next = temp
                    oddEnd = temp
                    oddEnd.next = evenBegin
                    curr = curr.next
                else:
                    break
            return head

        '''
        print "-"
        print curr.val
        print curr.next.val
        print oddEnd.val
        print oddEnd.next.val
        print evenBegin.val
        print evenBegin.next.val
        '''

            
