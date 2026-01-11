# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
   
    def isPalindrome(self, head):
        dummay1 = head
        stack = []
        while(dummay1 is not None):
            stack.append(dummay1.val)
            dummay1 = dummay1.next

        dummay2 = head
        while(dummay2 is not None):
            if stack[-1]!=dummay2.val:
                return False
            stack.pop()
            dummay2 = dummay2.next
        return True