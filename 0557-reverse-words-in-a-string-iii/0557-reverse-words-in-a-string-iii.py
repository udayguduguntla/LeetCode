class Solution:
    def reverseWords(self, s: str) -> str:
        # s=s.split(" ")
        # s=[i[::-1] for i in s]
        # return " ".join(s)

        return ' '.join(list(map(lambda s2 : s2[::-1], s.split())))