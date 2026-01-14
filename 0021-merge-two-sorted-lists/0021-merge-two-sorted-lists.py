# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if(not list1 and not list2):
            return list1

        ptr_1 = list1
        ptr_2 = list2
        dummy = ListNode(-1)
        curr = dummy
        while(ptr_1 and ptr_2):
            if(ptr_1.val <= ptr_2.val):
                curr.next = ptr_1
                ptr_1 = ptr_1.next
            else:
                curr.next = ptr_2
                ptr_2 = ptr_2.next
            curr = curr.next
        if(ptr_1):
            curr.next = ptr_1
        if(ptr_2):
            curr.next = ptr_2
        return dummy.next


        