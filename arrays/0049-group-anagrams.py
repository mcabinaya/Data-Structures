class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in map:
                map[sorted_s].append(s)
            else:
                map[sorted_s] = [s]
        
        result = []
        for k in map.keys():
            result.append(map[k])
        
        return result
