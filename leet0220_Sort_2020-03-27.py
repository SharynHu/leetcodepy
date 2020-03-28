# 桶排序
#每个桶的size为t，一共有k个桶，所有k个桶中的元素的index都在一个长度为k的窗口内。
#每个桶中只能有一个元素。如果有两个元素要加入同一个桶，说明它们的value difference小于等于t，这时候我们应该return True.
#并且当我们加入一个新元素的时候，如果t>0我们还应该检查它所在的桶左边的元素和右边的元素来确定有没有元素在范围[nums[i]-t, nums[i]+t]内。
#在加入元素的时候要注意保持window size<=k

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        buckets = {}
        for i in range(len(nums)):
            bucketNum = nums[i]/t if t else nums[i]
            offset = 0 if t==0 else 1
            for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
            
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                if t==0: 
                    buckets.pop(nums[i-k])
                else:
                    buckets.pop(nums[i-k]/t)
        return False
