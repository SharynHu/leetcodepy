#思路：将问题转化为从一个有序数组arr中找到最接近k个最target的值
#从小到大访问该有序数组，假设dist = [abs(num-target) for num in arr], 那么对于dist有三种可能：
#    1.先小后大
#    2.越来越大
#    3.越来越小
#在我们逐个访问arr数组中的元素时，一旦数组满了并且当前访问的元素的dist值大于先前访问的dist的最大值，我们就无需访问后续元素。

import heapq
class Solution(object):   
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        distance = []
        stack = [root]
        while(stack):
            while(stack and stack[-1].left):
                stack.append(stack[-1].left)
            while(stack):
                curr = stack.pop()
                currDist = abs(curr.val-target)
                if len(distance)<k:
                    heapq.heappush(distance, [-currDist, curr.val])
                else:
                    if currDist<(-distance[0][0]):
                        heapq.heappop(distance)
                        heapq.heappush(distance, [-currDist, curr.val])
                    else:
                        return sorted([val for distance, val in distance], reverse = True)
                if curr.right:
                    stack.append(curr.right)
                    break
                    
        return sorted([val for distance, val in distance], reverse = True)
        
