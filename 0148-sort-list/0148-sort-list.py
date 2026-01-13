class Solution(object):
    def merge(self, l_head, r_head):
        dummy = ListNode()
        curr = dummy

        while l_head and r_head:
            if l_head.val <= r_head.val:
                curr.next = l_head
                l_head = l_head.next
            else:
                curr.next = r_head
                r_head = r_head.next
            curr = curr.next

        curr.next = l_head if l_head else r_head
        return dummy.next


    

    def sort(self, head):
        if(head.next is None):
            return head
        fast = head
        right = head
        while(fast and fast.next):
            fast = fast.next.next
            right = right.next
        left = head
        temp = left
        while(temp.next!=right):
            temp = temp.next
        temp.next = None
        
        l_list = self.sort(left)
        r_list = self.sort(right)
        return self.merge(l_list, r_list)

    def sortList(self, head):
        if not head:
            return None
       
        return self.sort(head)
