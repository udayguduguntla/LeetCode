class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        prev_index = 0
        for index in spaces:
            result.append(s[prev_index:index])
            result.append(" ")
            prev_index = index
        result.append(s[prev_index:])
        return "".join(result)