# Two rules:
# rule1. The minimum is 1;
# rule2. higher rating students get higher candies that its neighbors;
# The difficulty of this problem lies in:
#   if ratings[i+1]>ratings[i], we know that we can allocate cadies[i]+1 to the (i+1)th child, there will be no violation of rule2. But if ratings[i+1]<=ratings[i+1], how many candies shall we allocate? if we choose the minimum 1, then, what about ratings[i+2]<ratings[i+1]? should we allocate 0? Of course NOT because we will be violating rule 1. 
#   So if the ratings are keeping strictly increasing, we know that 
#       candies[0] = 1;
#       candies[i+1] = candies[i];
#   If candies are composed of several strictly increasing ranges, for example:
#       [1,2,3,4],[3,4],[3],[2],[1]
#   For each range, we can apply the strategy above, Then we will get:
#       [1,2,3,4],[1,2],[1],[1],[1]
#   Now rule 1 is satisfied and rule 2 is locally satisfied(from left to right).
#   We need to merge the ranges to make sure that rule2 is globally satisfied. we know that if we only add some values of the last element of each range, it won't break rule2 for each range. Then how many should we add for each last element? For range i, it depends on range[i+1], so we need to scan the ranges backwards, then we'll get the result:
#       [1,2,3,4],[1,4],[3],[2],[1]
#   Acyually we do not need to find the end of each element. We just need to traverse the ratings array backwards.


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return []
        
        candies = [1]*len(ratings)
        #forward
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1]+1

        #backward
        for i in range(len(ratings)-2,-1, -1 ):
            if ratings[i]>ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
 
        return sum(candies)
        
