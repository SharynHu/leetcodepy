from math import ceil
class Solution(object):
    def check(self, distances, k, candidate):
        """
        count the maximum number of pieces we can have if we can slice those distances k times
        """
        j = len(distances)-1
        slices = 0
        while(j>=0):
            if distances[j]<=candidate:
                j -= 1
                continue
            slices += ceil(distances[j]/float(candidate))-1
            if slices>k:
                return False
            # count += slices
            # k -= slices-1
            j -= 1
        return slices<=k
    
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        left = 1.0/k
        right = stations[-1]-stations[0]
        distances = [stations[i+1]-stations[i] for i in range(len(stations)-1)]
        distances.sort()
        
        while(left+10**(-6)<right):
            middle = (left+right)/2.0
            if self.check( distances, k, middle):
                # we try finding a bigger one
                right = middle
            else:
                left = middle
        if self.check( distances, k, right):
            return right
        return left
