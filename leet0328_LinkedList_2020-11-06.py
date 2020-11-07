# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        oddHead = ListNode(0)
        o = oddHead
        evenHead = ListNode(0)
        e = evenHead
        p = head
        i = 0
        while(p):
            next_p = p.next
            p.next = None
            if i%2==1:
                o.next = p
                o = p
                p = next_p
            else:
                e.next = p
                e = p
                p = next_p
            i += 1

        e.next = oddHead.next
        return evenHead.next
