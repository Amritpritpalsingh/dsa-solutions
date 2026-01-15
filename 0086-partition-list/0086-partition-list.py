# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        curr = head
        less_than_head = ListNode(-1)
        less_than = less_than_head

        greater_than_head = ListNode(-1)
        greater_than =  greater_than_head
        while(curr):
            if(curr.val >= x ):
                greater_than.next = curr
                greater_than = greater_than.next
            else:
                less_than.next = curr
                less_than = less_than.next
            curr = curr.next
        
        greater_than.next = None
        less_than.next = greater_than_head.next
        return less_than_head.next

                






            








        