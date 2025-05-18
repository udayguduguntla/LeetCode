# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftTrav(self,root,l):
        if root:
            l.append(root.val)
            self.leftTrav(root.left,l)
            self.leftTrav(root.right,l)
        else:
            l.append(None)
        return l
    def rightTrav(self,root,l):
        if root:
            l.append(root.val)
            self.rightTrav(root.right,l)
            self.rightTrav(root.left,l)
        else:
            l.append(None)
        return l
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # l1=self.leftTrav(root.left,[])
        # l2=self.rightTrav(root.right,[])
        return self.leftTrav(root.left,[]) == self.rightTrav(root.right,[])