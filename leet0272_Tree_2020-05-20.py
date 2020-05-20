#思路：将问题转化为从一个有序数组arr中找到最接近k个最target的值
#从小到大访问该有序数组，假设dist = [abs(num-target) for num in arr], 那么对于dist有三种可能：
#    1.先小后大
#    2.越来越大
#    3.越来越小
#在我们逐个访问arr数组中的元素时，一旦数组满了并且当前访问的元素的dist值大于先前访问的dist的最大值，我们就无需访问后续元素。

import heapq
class Solution(object):
    def inorder(self, root, target, k, distance):
        if not root:
            return
        self.inorder(root.left, target, k, distance)
        currDist = abs(root.val-target)
        #如果当前的值还没满，那么将当前节点的距离加入distance并且更新values，并继续遍历右子树
        if len(distance)<k:
            heapq.heappush(distance, [-currDist, root.val])
            self.inorder(root.right, target, k, distance)
        else:
            #比较当前的distance和最大的distance的值
            #如果当前的distance比最大的distance的值要小，那么需要将较大的pop出来，放进当前值，并继续遍历右子树
            if currDist<(-distance[0][0]):
                heapq.heappop(distance)
                heapq.heappush(distance, [-currDist, root.val])
                self.inorder(root.right, target, k, distance)
            #如果当前的distance与最大的distance的值相等或者比其要大
            else:
                return
        
        
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        distance = []
        heapq.heapify(distance)
        self.inorder(root, target, k, distance)
        return sorted([val for distance, val in distance], reverse = True)
