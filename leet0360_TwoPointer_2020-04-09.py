class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a*x*x+b*x+c
        if not nums: 
            return []
        if len(nums)==1:
            return [f(nums[0])]
        
        if a<0:
            res = []
            i, j, k = 0, len(nums)-1, 0
            while(k<len(nums)):
                if f(nums[i])<=f(nums[j]):
                    res.append(f(nums[i]))
                    i += 1
                else:
                    res.append(f(nums[j]))
                    j -= 1
                k += 1
            return res
        else:
            res = []
            i, j, k = 0, len(nums)-1, 0
            while(k<len(nums)):
                if f(nums[i])>=f(nums[j]):
                    res.append(f(nums[i]))
                    i += 1
                else:
                    res.append(f(nums[j]))
                    j -= 1
                k += 1
            res.reverse()
            return res
       
