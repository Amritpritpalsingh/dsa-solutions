# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hA  = headA
        hB = headB
        map = {}
        while hA:
            if(hA not in map):
                map[hA] = 1
            else :
                map[hA] +=1
            hA = hA.next
        while(hB):
            if(hB in map):
                return hB
            hB = hB.next

        return  None
