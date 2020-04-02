class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charToIndex = {}
        
        maxLen = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in charToIndex:
                # add this char in our hashtable
                charToIndex[s[i]]=i
                continue
            #the current char has already been seen in a previous substring
            #preserve the length of a valid substring
            maxLen = max(maxLen, i-start)
            #find the previous occurance of the current char
            seenIndex = charToIndex[s[i]]
            #popout all the letters from start to seenIndex
            for j in range(start, seenIndex):
                charToIndex.pop(s[j])
            charToIndex[s[i]] = i
            #update start
            start = seenIndex+1
        maxLen = max(maxLen, len(s)-start)
        return maxLen
