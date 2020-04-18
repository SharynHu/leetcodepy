class Solution(object):
    def compare(self, num1, denum1, num2, denum2):
        #判断分数num1/denum1是否大于num2/denum2
        return num1*denum2>denum1*num2
    
    def calVal(self, A, mid_num, mid_denum):
        count, n = 0, len(A)
        #j标记的是分母的坐标，分母从A[1]开始，到A[n-1]结束
        j =  1
        #i标记的是分子的坐标，分子从A[0]开始到A[n-2]结束
        p, q = 1,1
        k, v = 0, 1
        for i in range(len(A)-1):
            #note that j starts from i+1
            #寻找第一个大于当前middle的值的数
            while(j<len(A) and self.compare(A[i], A[j], mid_num, mid_denum)):
                if self.compare(p, q, A[i], A[j]):
                    p, q = A[i], A[j]
                j += 1
            if j<len(A) and not self.compare(k, v, A[i], A[j]):
                k, v = A[i], A[j]
            j = max(j, i+1)
            count += n-j
        return count, p, q, k, v
            
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        start_num, start_denum = 0, 1
        end_num, end_denum = 1, 1
        while(self.compare(end_num, end_denum, start_num, start_denum)):
            #计算中间分数
            middle_num = start_num*end_denum+end_num*start_denum 
            middle_denum = start_denum*end_denum*2
            count, p, q, k, v = self.calVal(A, middle_num, middle_denum)
            if count<K:
                #说明当前的middle值小了，我们需要将start值更新为最小的比middle大的值
                start_num, start_denum = p, q
            else:
                #将当前的middle值更新为最大的不大于middle的值
                end_num, end_denum = k,v
        return [start_num, start_denum]
