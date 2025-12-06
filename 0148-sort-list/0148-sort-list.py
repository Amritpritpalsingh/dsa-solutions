class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # 1. Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None   # break the list
        
        # 2. Sort each half
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # 3. Merge sorted halves
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next
