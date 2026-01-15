# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev_ll(self,head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next     # save next node
            curr.next = prev    # reverse pointer
            prev = curr         # move prev forward
            curr = nxt          # move curr forward

        return prev

    def reorderList(self, head):
        res_head = ListNode(0)
        curr = res_head
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        middle = slow.next
        slow.next = None
        orginal_ll = head
        reverse_ll = self.rev_ll(middle)
        while(reverse_ll is not None and orginal_ll is not None):
            curr.next = orginal_ll
            curr=curr.next
            orginal_ll = orginal_ll.next
            curr.next = reverse_ll
            curr=curr.next
            reverse_ll = reverse_ll.next
            
        if(reverse_ll):
            curr.next = reverse_ll
        if(orginal_ll):
              curr.next = orginal_ll
        return res_head.next


        
        
        

            

        