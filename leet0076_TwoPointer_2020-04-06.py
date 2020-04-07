class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        tCount = collections.Counter(t)
        sCount = collections.defaultdict(int)
        i, j, goal, cnt = 0, 0, len(tCount), 0
        minLen = float('inf')
        minStr = ""
        
        while(j<len(s)):
            if s[j] in tCount:
                sCount[s[j]] += 1
                #只有==的时候cnt才能增加，因为cnt只能被增加一次
                if sCount[s[j]] == tCount[s[j]]:
                    cnt +=1 
            #current string is s[i:j+1]
            #check if the current string is valid
            while(i<=j and cnt == goal):
                #first update the minStr and minLen
                if j-i+1<minLen:
                    minLen = j-i+1
                    minStr = s[i:j+1]
                # then we move i rightforward to see if we can find a shorter valid substring
                if s[i] in tCount:
                    #update cnt and sCount
                    sCount[s[i]] -= 1
                    if sCount[s[i]] < tCount[s[i]]:
                        cnt -= 1
                i += 1
            j += 1
        return minStr
