#二叉树的最大深度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #叶子节点的判断
        if root == None:
            return 
        
        #递归分解
        leftmax = self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)
        #最大深度为左右子树的最大深度加一
        return 1 + max(leftmax,rightmax)

