# We need to note that nums1 is the subset of nums2. So we can definitely find each element of nums1 in nums2.
# For each element in nums2, we can only search to its right and get the first elment greater than it.
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashMap = {}
        # stack is to keep a decreasing subarray of nums2
        stack = []
        res = []
        
        for num in nums2:
            #current number is num. If it makes stack decreasing, we add it into the stack.
            if not stack or stack[-1]>=num:
                stack.append(num)
                continue
            # if the current number is bigger than top of te stack, then it is the first element bigger than stack[-1]. For each element in the stack we need to check if it is greater than that element.
            while(stack and stack[-1]<num):
                hashMap[stack.pop()] = num
            stack.append(num)
        return [hashMap.get(num, -1) for num in nums1]
