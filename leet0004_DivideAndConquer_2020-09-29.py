class Solution(object):
    def getKthSmallest(self, A, B, k):
        """
        find the kth samllest number in A and B
        """
        #1. Make B the longer one
        if len(A)>len(B):
            A, B = B, A
        #2. corner cases
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        #3. divide A and B both into two parts A[:pa] B[:pb]. The first two parts of A and B have k elements in total.
        pa = min(k/2, len(A))
        pb = k-pa
        #4. If A[pa-1]<=B[pb-1], this means that any element in Apart1 cannot be the K-th smallest element, we just discard them.
        # This is because if the K-th element is in Apart1, then there will be less than k-1 numbers smaller than the K-th element.
        if A[pa-1]<=B[pb-1]:
            return  self.getKthSmallest(A[pa:], B, pb)
        #5. If A[pa-1]>B[pb-1], same here, any element in Bpart1 cannot be the K-th smallest element, we just discard them.
        return self.getKthSmallest(A, B[pb:], pa)
    
         
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2))%2==1:
            return self.getKthSmallest(nums1, nums2, (len(nums1)+len(nums2)+1)/2)
        else:
            return (self.getKthSmallest(nums1, nums2, (len(nums1)+len(nums2))/2)+self.getKthSmallest(nums1, nums2, (len(nums1)+len(nums2))/2+1))/2.0
