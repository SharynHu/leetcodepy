class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        counter = collections.Counter(words)
        m = len(words[0])
        n = len(words)
        res = []
        
        for i in range(m):
            windowCount = collections.defaultdict(int)
            window = []
            
            for j in range(i, len(s), m):
                word = s[j:j+m]
                #if the current word not in words, then any substring containing current word won't satisfy the condition. so we need to clear localCount and window and start over.
                if word not in counter:
                    window = []
                    windowCount.clear()
                    continue
                #if the current  word is in words, then first we update the local count and the window
                windowCount[word] += 1
                window.append(word)
                # if current word counts more in the window than in words, then we need to pop some words out from the window until we have less or equal number of "word" in current window.
                while(windowCount[word]>counter[word]):
                    windowCount[window.pop(0)] -= 1
                # check if the current window satisfy the condition
                if len(window) == n:
                    res.append(j-(n-1)*m)
        return res
