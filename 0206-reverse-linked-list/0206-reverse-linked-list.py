# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        newHead = prev
        while(curr):
            prev = curr
            curr = curr.next
            prev.next = newHead
            newHead = prev
        return prev



            