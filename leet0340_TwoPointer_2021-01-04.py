class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k==0:
            return 0
        
        i, j = 0, 0
        charToIndex = {}
        maxLen = 0
        
        while(j<len(s)):
            #if the current char has already been in hashmap, it means we still have at most two distinct charaters in the current window
            if s[j] in charToIndex:
                charToIndex[s[j]] = max(charToIndex[s[j]], j)
                maxLen = max(j-i+1, maxLen)
                j += 1
                continue
            # if we meet a new char
            if len(charToIndex)<=k-1:
                charToIndex[s[j]] = j
                maxLen = max(maxLen, j-i+1)
                j += 1
                continue
            # we need to pop out some chars
            if i==charToIndex[s[i]]:
                charToIndex.pop(s[i])
            i += 1
        return maxLen
    
        
