 class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        list1 = [2]
        list2 = [3]
        list3 = [5]
        
        i = 1
        while(i<n):
            curr=min(list1[0], list2[0],list3[0])
            if curr==list1[0]:
                list1.pop(0)
            if curr==list2[0]:
                list2.pop(0)
            if curr==list3[0]:
                list3.pop(0)
            if curr == prev:
                continue
            i += 1
            prev = curr
            list1.append(curr*2)
            list2.append(curr*3)
            list3.append(curr*5)
        return prev
