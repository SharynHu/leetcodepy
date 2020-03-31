class Solution(object):
    def compare(self, num1, num2):
        a = num1*(10**len(str(num2)))+num2
        b = num2*(10**len(str(num1)))+num1
        if a<b:return -1
        if a==b:return 0
        return 1
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(reverse=True, key=functools.cmp_to_key(self.compare))
        res =  ''.join(map(str, nums))
        #去除头部的0
        return str(int(res))
