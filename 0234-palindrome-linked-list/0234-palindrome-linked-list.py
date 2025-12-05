# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        dummy = head
        stack = []
        while dummy:
            stack.append(dummy)
            dummy = dummy.next
        for i in range(len(stack)):
            if(stack[len(stack)-1-i].val == head.val):
                head=head.next
            else :
                return False
        return True
        