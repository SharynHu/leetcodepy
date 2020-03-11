class Solution(object):
    def findMaxForm(self, strs, n, m):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = set([(0,0,0)])
        for string in strs:
            numOnes = sum(map(int, list(string)))
            numZeros = len(string)-numOnes
            newDp = set()
            for x, y, z in dp:
                newDp.add((x, y, z))
                if x+numOnes<=m and y+numZeros<=n:
                    newDp.add((x+numOnes, y+numZeros, z+1))
            dp = newDp
        return max([z for x,y,z in dp])
