# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None : return None
        ha  = headA
        hb = headB
        while(ha!= hb):
            ha = ha.next
            hb = hb.next
            if(hb==ha):return ha
            if(ha is None):
                ha = headB
            if(hb is None):
                hb = headA
        return ha
        


