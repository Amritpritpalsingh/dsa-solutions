class Solution(object):
    def detectCycle(self, head):
        if(head==None):return head
        if(head.next is None):
            return None
        isCycle = -1
        fast = head
        slow = head
        map = {}
        while fast and fast.next:
            if slow not in map:
                map[slow] = 1
            else:
                return slow
            fast = fast.next.next
            slow = slow.next
        if(isCycle==-1):
             return None


        
            
        
        
            
        