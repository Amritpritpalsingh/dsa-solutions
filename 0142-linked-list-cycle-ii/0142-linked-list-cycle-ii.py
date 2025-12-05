class Solution(object):
    def detectCycle(self, head):
        if(head==None):return head
        if(head.next is None):
            return None
        isCycle = -1
        slow = head
        map = {}
        while slow and slow.next:
            if slow not in map:
                map[slow] = 1
            else:
                return slow
            slow = slow.next
        
        return None


        
            
        
        
            
        