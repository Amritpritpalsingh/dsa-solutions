# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if (not headA or not headB):
            return headA
        ptr_a = headA
        ptr_b = headB
        while(ptr_a != ptr_b):
            if(ptr_a):
                ptr_a = ptr_a.next
            else:
                ptr_a= headB

            if(ptr_b):
                ptr_b= ptr_b.next
            else:
                ptr_b= headA
        
        return ptr_a