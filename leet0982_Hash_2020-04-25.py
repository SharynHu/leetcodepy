#思路：A[i]&A[j]的值最多有2**16个不同的，可以将它们都放进hashMap中，冰书厨每一个值出现的次数
#对于每个A[k]验证A[i]&A[j]是否为0
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashMap = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(A)):
                hashMap[A[i]&A[j]] += 1
        
        res = 0
        for k in range(len(A)):
            for val in hashMap:
                if (A[k]&val)==0:
                    res += hashMap[val]
        return res
