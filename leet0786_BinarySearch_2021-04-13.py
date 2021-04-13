#注：由于A中的数都是质数并且p<q， 所以分数中应该没有duplicates。
#我们可以先对A进行去重。
# 由于分数没有duplictates，所以第k个分数也没有重复值，这样的话在区间(0, 1)之间一定存在一个数，在所有的分数中有K个数大于等于它。
import bisect
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        start, end = 0, 1
        A = list(set(A))
        A.sort()
        while(start<end):
            middle = (start+end)/2.0
            
            j = 0
            border = []
            for i in range(len(A)):
            # find the maximum A[i]/A[j] (rightmost) that is smaller or equal to than candidate 
            # that is to find the minimum A[j] such that A[j]>=A[i]/candidate
                j = bisect.bisect_left(A, float(A[i])/middle, j, len(A))
                border.append(j)
            count = sum([len(A)-j for j in border])
            if count<K:
                start = middle
            if count>K:
                end = middle
            if count==K:
                # the maximum fraction less than or equal to middle is the result
                res = [0,1]
                for i in range(len(A)):
                    if border[i]<len(A):
                        if A[i]/float(A[border[i]])>=float(res[0])/res[1]:
                            res = [A[i], A[border[i]]]
                return res
