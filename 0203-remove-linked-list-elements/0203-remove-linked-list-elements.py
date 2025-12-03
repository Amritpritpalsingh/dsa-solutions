class Solution(object):
    def removeElements(self, head, val):
        dummy =  ListNode(0)
        dummy.next = head
        curr = dummy
        while(curr.next is not None):
            if(curr.next.val != val):
                 curr = curr.next
            else:
                curr.next = curr.next.next
       
        return dummy.next
        
            
        
