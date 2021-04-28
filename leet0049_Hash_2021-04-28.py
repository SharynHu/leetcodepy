# if we sort two anagrams, they will the same
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)
        res = []
        for key in hashmap:
            res.append(hashmap[key])
        return res
