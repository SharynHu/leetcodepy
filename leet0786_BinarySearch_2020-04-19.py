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
            #计算中间分数
            mid = (start+end)/2.0
            #i表示分子的坐标， j表示分母的坐标
            #对于每一行，找到第一个index使得A[j]>=A[i]/mid，这样所有在j及j右边的所有值都满足A[i]/A[j]<=mid
            border = [bisect.bisect(A, A[i]/float(mid)) for i in xrange(len(A))]
            #计算所有小于等于mid的分数的个数
            count = sum([len(A)-j for j in border])
            print mid, count
            if count<K:
                #说明第k小的值在区间[middle, end]之间
                start = mid
            if count>K:
                #说明第k小的值在区间[start, end]之间
                end = mid
            if count==K:
                print mid, count, border
                #那么此时最大的小于等于mid的值就是第k小的值
                res = [0,1]
                for i in range(len(A)):
                    if border[i]<len(A):
                        if A[i]/float(A[border[i]])>=float(res[0])/res[1]:
                            res = [A[i], A[border[i]]]
                return res
        
