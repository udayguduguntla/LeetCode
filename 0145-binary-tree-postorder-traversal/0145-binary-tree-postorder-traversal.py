# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.li=[]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left, right, root //post
        #left, root, right //in
        #root, left, right //pre
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.li.append(root.val)
        return self.li
