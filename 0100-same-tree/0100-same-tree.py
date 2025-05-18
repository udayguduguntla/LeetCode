# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTrav(self,root,l):
        if root:
            l.append(root.val)
            self.preorderTrav(root.left,l)
            self.preorderTrav(root.right,l)
        else:
            l.append(None)
        return l
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1=self.preorderTrav(p,[])
        l2=self.preorderTrav(q,[])
        print(l1,l2)
        return l1==l2