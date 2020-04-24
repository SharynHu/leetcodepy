#两个字符串互为anagram的条件是它们的字母及字母数一样
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(s)<len(p):
            return []
        
        charSet = set(p)
        countS = collections.defaultdict(int)
        start, end, curr, goal, res = 0, 0, 0, len(charSet), []
        countP = collections.Counter(p)
        while(end<len(s)):
            if s[end] not in charSet:
                start = end+1
                end = start
                countS.clear()
                curr = 0
                continue
            countS[s[end]] += 1
            #s[start:end+1]这一段字符串中是不包含任何其他字母的
            while(countS[s[end]]>countP[s[end]]):
                if countS[s[start]] >= countP[s[start]]:
                    curr -= 1
                countS[s[start]] -= 1
                start += 1
            #现在s[start:end+1]满足只包含p中的字母并且每个字母的个数不超过p中字母的个数
            if countS[s[end]] == countP[s[end]]:
                curr += 1
            if curr == goal:
                res.append(start)
            #寻找下一个解
            end += 1
        return res
