# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p,q = head, head
        while(q.next):
            p = p.next
            if q.next and q.next.next:
                q = q.next.next
                continue
            break
        return p
