class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []
        
        for i in range(max_len):
            vertical_word = "".join(word[i] if i < len(word) else " " for word in words)
            result.append(vertical_word.rstrip())
        
        return result
