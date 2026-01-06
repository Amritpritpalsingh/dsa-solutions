# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self,head):
    
        new_head = None
        curr = head
        length = 0
        while curr:
            node = ListNode(curr.val)   # create new node
            node.next = new_head        # reverse link
            new_head = node
            curr = curr.next
            length +=1 

        return new_head,length

    def reorderList(self, head):
        if(head is None or head.next is None):return None
        r_ptr = head
        rHead,length = self.rev(head)
        result_head = ListNode(-1)
        dummyH = result_head
        l_ptr = rHead
        if(length%2==0):
            for i in range(length//2):
                dummyH.next = r_ptr
                r_ptr = r_ptr.next
                dummyH=dummyH.next

                dummyH.next  = l_ptr
                l_ptr = l_ptr.next
                dummyH =dummyH.next
            dummyH.next = None
        else:
            for i in range((length-1)//2):
                dummyH.next = r_ptr
                r_ptr = r_ptr.next
                dummyH=dummyH.next

                dummyH.next  = l_ptr
                l_ptr = l_ptr.next
                dummyH =dummyH.next
           
            dummyH.next.next = None
            
        return result_head.next


            
        


        
            


        