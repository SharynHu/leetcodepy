class Solution(object):
    def findx(self, arr, x):
        left, right= 0, len(arr)-1
        while(left+1<right):
            middle = (left+right)/2
            if arr[middle]>x:
                right = middle
            else:
                left = middle
        return left, right
    
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = self.findx(arr, x)
        res = []
        
        if left==right:
            return [arr[left]]

        while(len(res)<k):
            if left<0 and right>=len(arr):
                break
            if left<0:
                res.append(arr[right])
                right += 1
                continue
            if right>=len(arr):
                res.append(arr[left])
                left -= 1
                continue
            if abs(arr[left]-x)<abs(arr[right]-x):
                res.append(arr[left])
                left -= 1
            elif abs(arr[left]-x)>abs(arr[right]-x):
                res.append(arr[right])
                right += 1
            else:
                res.append(arr[left])
                left -= 1
        res.sort()
        return res
