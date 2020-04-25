class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        res = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            #如果不是连续的，那么需要另开一个
            if nums[i]>res[-1][-1]+1:
                res.append([nums[i], nums[i]])
            #如果当前的数字与之前的数字相等，那么res数组保持不变
            if nums[i] == res[-1][-1]:
                continue
            #如果是连续的那么改变之前最后一个end的值
            if nums[i]==res[-1][-1]+1:
                res[-1][-1] += 1
        return [str(start) if start==end else str(start)+"->"+str(end) for (start, end) in res]
                
