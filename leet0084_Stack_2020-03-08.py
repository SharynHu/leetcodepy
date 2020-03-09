# 但是向左右遍历寻找比他小的bar的时间复杂度是O(n)，在加上遍历一遍所有的bar，总的时间复杂度将为O(n*n)，是无法通过所有数据的。因此我们需要寻找一种时间复杂度更低的寻找一个bar左右边界的算法。
# 在网上流传了一个设计极其巧妙的方法，借助一个stack可以将时间复杂度降为O(n);这种算法的思想是维护一个递增的栈，这个栈保存了元素在数组中的位置。 这样在栈中每一个左边的bar都比本身小，所以左边就天然有界了，也就是左边界就是左边的一个bar。遍历一遍height数组，在将height数组入栈的时候，如果当前元素heights[i]比栈顶元素小，则我们又找到了栈顶元素的右边界。因此我们在此时就可以计算以栈顶元素为最低bar的矩形面积了，因为左右边界我们都已经找到了，而且是在O(1)的时间复杂度内找到的。然后就可以将栈顶元素出栈了。这样每出栈一个元素，即计算以此元素为最低点的矩形面积。当最终栈空的时候我们就计算出了以所有bar为最低点的矩形面积。为保证让所有元素都出栈，我们在height数组最后加一个0，因为一个元素要出栈必须要遇到一个比他小的元素，也就是右边界。

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        
        heights.append(0)
        maxArea = 0
        stack = [-1]
        for i in range(len(heights)):
            #栈中只有-1， 那么把当前的index入栈
            if len(stack)==1:
                stack.append(i)
                continue
            #如果当前index的高度大于等于栈顶元素的高度， 我们尚未找到栈顶元素的右边界， 此时需要将当前index放入栈中
            if heights[i]>=heights[stack[-1]]:
                stack.append(i)
                continue
            #如果当前index的高度小于栈顶元素的高度，那么我们找到了栈顶元素的右边界， 此时计算面积
            while(len(stack)>1 and heights[i]<heights[stack[-1]]):
                top = stack.pop()
                maxArea = max(maxArea, (i-stack[-1]-1)*heights[top])
            #stack中所有index的高度都比当前index小，我们将当前index压入栈
            stack.append(i)
        return maxArea
