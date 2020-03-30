class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if not rating or len(rating)<3:
            return 0
        
        #对于每个i计算左边比它小的元素的个数
        smaller_left = [0]*len(rating)
        #对于每个i计算左边比它大的元素的个数
        bigger_left = [0]*len(rating)
        #对于每个i计算右边比它大的元素的个数
        bigger_right = [0]*len(rating)
        #对于每个i计算右边比它小的元素的个数
        smaller_right = [0]*len(rating)
        
        for i in range(len(rating)):
            for j in range(len(rating)):
                if rating[j]<rating[i] and j<i:
                    smaller_left[i] += 1
                if rating[j]>rating[i] and j>i:
                    bigger_right[i] += 1
                if rating[j]<rating[i] and j>i:
                    smaller_right[i] += 1
                if rating[j]>rating[i] and j<i:
                    bigger_left[i] += 1
                    
        res  = 0
        for i in range(len(rating)):
            res += smaller_left[i]*bigger_right[i]+bigger_left[i]*smaller_right[i]
        return res
