# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):               
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        #split list into twonparts, part1 is processed, we mark its head as start1 and end1
        # part2 is unprocessed, we mark its head as start2
        start1, end1 = dummy, dummy
        start2 = head
        while(start2):
            #find 3 pivots
            p = start2
            for i in range(k-1):
                if p and p.next:
                    p = p.next
                else:
                    #No need to reverse nodes[start2:p+1]
                    end1.next = start2
                    return dummy.next
            #mark the new start2
            newStart2 = p.next
            p.next = None
            #reverse nodes[start2:p+1]
            dummyEnd = None
            p = start2
            for j in range(k):
                nextNode = p.next
                p.next = dummyEnd
                dummyEnd = p
                p = nextNode
            #Now we've reversed nodes[start2:p+1] and the head of the reversed part is dummyEnd, we need to append this new head to end1
            end1.next = dummyEnd
            end1 = start2
            start2 = newStart2
        return dummy.next
