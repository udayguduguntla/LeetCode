class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = popped[::-1]
        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
        if stack == popped:
            return True
        return not stack