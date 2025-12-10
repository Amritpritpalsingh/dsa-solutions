# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sL = ListNode(-1)
        curr = sL
        t1 = l1
        t2 = l2
        carry = 0
        while(t1 and t2):
            s = t1.val+t2.val+carry
            carry = s//10
            newN = ListNode(s%10)
            curr.next  = newN
            curr = newN
            t1 = t1.next
            t2 = t2.next
        while(t1):
            s = t1.val+carry
            carry = s//10
            newN = ListNode(s%10)
            curr.next  = newN
            curr = newN
            t1 = t1.next
        while(t2):
            s = t2.val+carry
            carry = s//10
            newN = ListNode(s%10)
            curr.next  = newN
            curr = newN
            t2 = t2.next
        if(carry!=0):
            newN = ListNode(carry)
            curr.next  = newN
            curr = newN



        return sL.next