class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        left, right = 0, len(citations)-1
        
        while(left+1<right):
            middle = (left+right)/2
            h = len(citations)-middle
            #check if h papers have at least h citations
            if citations[middle]>=h:
                # check if other N-h paper have no more than h citations
                if  citations[middle-1]<=h:
                    return len(citations)-middle  
                else:
                    right = middle-1
            else:
                left = middle
        
        
        # check left and right
        if citations[left]>=len(citations)-left:
                if left == 0 or citations[left-1]<=len(citations)-left:
                    return len(citations)-left
                
        if citations[right]>=len(citations)-right:
                if right == 0 or citations[right-1]<=len(citations)-right:
                    return len(citations)-right
        return 0
