# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if(head is None or head.next is None):
            return False
        slow = head
        fast = head
        while(fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                return True
        return False


        