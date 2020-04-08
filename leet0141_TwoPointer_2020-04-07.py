# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# a fast and a slow pointer
# check whether they'll meet
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next or not head.next.next:
            return False
        
        slow = head
        fast = head
        while(fast and fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
