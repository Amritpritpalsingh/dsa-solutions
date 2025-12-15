# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if(head is None or head.next is None):
            return head
        lens = 0
        l = head
        while(l):
            l = l.next
            lens+=1

        for i in range(k%lens):
            temp = head
            prev = None
            while(temp.next):
                prev = temp
                temp = temp.next
            prev.next  = None
            temp.next = head
            head = temp
        return head
        


        