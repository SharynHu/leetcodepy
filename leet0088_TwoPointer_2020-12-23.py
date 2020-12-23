class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # the key point lies in we need to maintain nums2 sorted. if we have an extra array to save the result, it will be an easy question because we do not put any element of nums2 into nums1 or any element of nums1 into nums2.
        # to avoid the problem if mixing the two arrays, we need utilize the "extra space".
        # the solution is to start merging in reverse order.
        
        i = m-1
        j = n-1
        k = m+n-1
        while(k>=0):
            if (i>=0 and j>=0 and nums1[i]>=nums2[j]) or j<0:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
                continue
            if (i>=0 and j>=0 and nums2[j]>=nums1[i]) or i<0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
                continue
            
                
            
