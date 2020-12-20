class Solution(object):
    def check(self, sub, m, n, count, currCount):
        for i in range(n):
            word = sub[i*m:i*m+m]
            currCount[word] += 1
            if currCount[word]>count[word]:
                return False
        return True

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        m = len(words[0])
        n = len(words)
       
        res = []
        count = collections.Counter(words)
        
        for i in range(len(s)):
            sub = s[i:i+m*n]
            currCount = collections.defaultdict(int)
            if self.check(sub, m, n, count, currCount):
                res.append(i)
        return res
        
