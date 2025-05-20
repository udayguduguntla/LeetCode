from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            dict[key].append(i)
        return list(dict.values())