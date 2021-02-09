# this is equivalent to a matrix where each row and column are ascending, find the k smallest elements (leetcode 378)
# if the k-th smallest elements is duplicated, then we may have less than k-1 elments smaller than it.
# so to solve this problem, we need to count the number of elements less than candidate, and find the minimum(leftmost) one that has the count >=k

class Solution(object):
    def count(self, nums1, nums2, candidate):
        i, j, cnt = 0, len(nums2)-1, 0
        for i in range(len(nums1)):
            while(j>=0 and nums1[i]+nums2[j]>candidate):
                j -= 1
            # now nums1[i]+nums1[j]<=candidate and they are the biggest element in a row, which means in this row all elements before(including) nums[i][j] <=candidate
            # we update cnt here
            cnt += j+1
            # because nums[i][j+1]>candidate, so in the next row we do not need to update j
        return cnt
                     
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not k or not nums1 or not nums2:
            return []
        
        res = []
        left = nums1[0]+nums2[0]
        right = nums1[-1]+nums2[-1]
        
        while(left+1<right):
            middle = (left+right)/2
            cnt = self.count(nums1, nums2, middle)
            if cnt<k:
                left = middle
            else:
                right = middle
        # check left and right
        if self.count(nums1, nums2, left)>=k:
            k_th = left
        else:
            k_th = right

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]+nums2[j]<k_th:
                    res.append([nums1[i], nums2[j]])
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]+nums2[j]==k_th:
                    res.append([nums1[i], nums2[j]])
        return res[:k]
        
