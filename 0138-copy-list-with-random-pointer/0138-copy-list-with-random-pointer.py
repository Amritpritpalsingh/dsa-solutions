"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        temp = head

        while(temp):
            nn = Node(temp.val)
            nn.next = temp.next
            temp.next = nn
            temp = temp.next.next

        temp = head
        while(temp):
            copyNode = temp.next
            if(temp.random):
                copyNode.random = temp.random.next
            else:
                 copyNode.random  = None
            temp = temp.next.next
        dummy  = Node(-1)
        headD = dummy
        temp = head
        while(temp):
            dummy.next = temp.next
            dummy = dummy.next
            temp.next = temp.next.next
            temp = temp.next

        return headD.next





        