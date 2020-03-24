class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dpLen记录以index i结尾的最长子序列的长度
        dpLen = [1]*len(nums)
        #dpCount记录以index i结尾的最长子序列的个数
        dpCount = [1]*len(nums)
        
        res = 0
        maxLen = 0
        
        for i in range(len(nums)):
            for j in range(i):
                #我们需要找到i之前所有满足nums[j]<nums[i]的最长子序列
                if nums[j]>=nums[i]:
                    continue
                # 如果 len[i] 等于 len[j] + 1，说明 nums[i] 这个数字可以加在以 nums[j] 结尾的递增序列后面，并且以 nums[j] 结尾的递增序列个数可以直接加到以 nums[i] 结尾的递增序列个数上。如果 len[i] 小于 len[j] + 1，说明找到了一条长度更长的递增序列，那么此时将 len[i] 更新为 len[j]+1，并且原本的递增序列都不能用了，直接用 cnt[j] 来代替。
                if dpLen[i]==dpLen[j]+1:
                    dpCount[i] += dpCount[j]
                elif dpLen[i]<dpLen[j]+1:
                    dpLen[i] = dpLen[j]+1
                    dpCount[i] = dpCount[j]
            #更新最大长度
            #如果当前的长度等于最大长度， 那么将它的个数加入最大长度的个数
            if dpLen[i] == maxLen:
                res += dpCount[i]
            if dpLen[i]>maxLen:
                maxLen = dpLen[i]
                res = dpCount[i]
           
        
        return res
