# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if(head is None or head.next is None):
            return False
        from collections import defaultdict
        
        map = defaultdict(ListNode)
        temp = head
        while(temp.next is not None):
            if(temp in map):
                return True
            else:
                map[temp] = 0
            temp = temp.next
        return False


        