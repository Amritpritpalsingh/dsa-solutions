# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        nhead=None
        while head:
            newNode = ListNode(head.val)
            if(nhead is None):
                nhead = newNode
            else:
                newNode.next = nhead
                nhead = newNode
            head=head.next
        return nhead


            