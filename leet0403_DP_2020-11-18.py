class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1]!=1:
            return False
        
        # for each stone, we record the jump length to reach it
        d = dict((x, set()) for x in stones)
        d[1].add(1)
        for i in range(1, len(stones)-1):
            for j in list(d[stones[i]]):
                # we reach the current stone using j steps, and we can reach the next stone using j-1,j,j+1 steps
                for k in range(j-1, j+2):
                    if stones[i]+k in d:
                        d[stones[i]+k].add(k)
        return len(d[stones[-1]])>0
