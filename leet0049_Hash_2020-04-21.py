#annagram就是指两个词的字母及字母个数是一样的，只是字母的顺序不一样
#两个词是anagram当且仅当它们排序后得到的字符串是一样的
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = collections.defaultdict(list)
        
        for string in strs:
            key = tuple(sorted(string))
            hashMap[key].append(string)
        
        res = []
        for key in hashMap:
            res.append(hashMap[key])
        return res
