class Solution(object):
    def oddEvenList(self, head):
        if(head is None or head.next is None):return head
        even = head.next
        odd = head
        evenHead = head.next
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head

            


        