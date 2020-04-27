# 使用left和right来定界每一步所能达到的范围。则再下一步所能达到的范围，只要从nums[left]到nums[right]开始推算即可。不断依次推进，更新left和right，直至right抵达末尾。这期间走过了几步，就是最终答案。
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        steps = 0
        while(right<len(nums)-1):
            #当前可能在left和right之间的任意位置
            newLeft = float('inf')
            for i in range(left, right+1):
                newLeft  = min(newLeft, i+(nums[i]>0))
                right = max(right, i+nums[i])
            left = newLeft   
            steps += 1
        return steps
