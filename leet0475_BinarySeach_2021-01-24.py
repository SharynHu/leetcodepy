# This problem is:
#    for each element nums[i] in nums1, find a minimum distance min([abs(nums1[i]-nums2[j]) for j in range(len(nums2))]).
# and return the maximum minimim distance
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        standard = float('-inf')
        for i in range(len(houses)):
            # corner cases
            # 1. if all the heaters are on the left side of houses[i]
            if heaters[-1]<=houses[i]:
                standard = max(standard, houses[i]-heaters[-1])
                continue
            # 2. if all the heaters are on the right side of houses[i]
            if heaters[0]>=houses[i]:
                standard = max(standard, heaters[0]-houses[i])
                continue
            
            # try to find the "zero" point of the line
            left, right =0, len(heaters)-1
            while(left+1<right):
                middle = (left+right)/2
                if heaters[middle]-houses[i]<0:
                    left = middle
                else:
                    right = middle
            standard = max(standard, min(abs(heaters[left]-houses[i]), abs(heaters[right]-houses[i])))
        return standard
                
        
