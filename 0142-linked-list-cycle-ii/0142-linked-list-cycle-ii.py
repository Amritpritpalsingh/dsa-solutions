# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if(head==None):return head
        if(head.next is None):
            return None
        isCycle = -1
        pos = -1
        fast = head
        slow = head
        l = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            l+=1
            if(slow==fast):
                isCycle = 1
                if(l%2 == 0):
                    return fast
                else: return fast.next
        if(isCycle==-1):
             return None


        
            
        
        
            
        