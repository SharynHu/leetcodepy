# idea: 
        # 7 2 5 (2) 3 1
        # 7 2 5 3 (1) 2
        # 7 (2) 5 3 2 1
        # 7 3 1 2 (2) 5
        # 其中()中的数字表示next permutation改变原数字的最高位。比如对于725321来说，由于5321由于从最低位到最高位是升序排列，已经达到该四位数字permutation的最大值。这时不得不改变第5位的2来增加数值。如何改变？为了使增量最小，在（5，3，2，1）中找一个最小的比2大的数，即数字3。用3替换2，而剩下5, 2, 2, 1四个数字要组成最低4位。由于第2位已经从2增加到3，同样为了使增量最小，我们希望剩下的最后4位数尽可能小。
        #1. 从低位向高位（从右向左）找第一个递减的数：s[i]<s[i+1]。如果不存在，则表明该permutation已经最大，next permutation为当前序列的逆序。
        #2. 在s[i+1:]中找一个最小的s[j]，使得s[j]>s[i], 也就是说s[j]>s[i]>=s[j+1], 交换s[i], s[j]。
        #3. 对s[i+1:]进行排序。 由于s[i]>=s[j+1]，所以s[i+1:]实际上为降序排列，我们只需将 s[i+1:]逆序。
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)<=1:
            return 
        #1. 从右向左寻找第一个非降序元素
        j = len(nums)-1
        # 注意等号
        while(j-1>=0 and nums[j-1]>=nums[j]):
            j -= 1
        if j == 0:
            # 这就意味着nums是全降序排列，我们只需将其倒序就行。
            for i in range(len(nums)/2):
                nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
            return 
        
        j = j-1
        # 2. 已经找到第一个非降序元素为nums[j],从又往左找到第一个比它大的数
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>nums[j]:
                break

        # 3. 交换这两个数并且将降序部分升序排列
        nums[i], nums[j] = nums[j], nums[i]
        # 注意从j+1开始排列
        for k in range(j+1, j+1+(len(nums)-j)/2):
            print k, len(nums)-1-k
            nums[k], nums[j+1+len(nums)-1-k] = nums[j+1+len(nums)-1-k], nums[k]
        return
