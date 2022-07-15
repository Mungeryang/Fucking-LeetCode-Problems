#反转二叉树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#分解问题
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #判断根节点
        if root == None:
            return
        #反转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        #后序操作
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root

#遍历思路
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.travser(root)
        return root
    def travser(self,root):
        if root == None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.travser(root.left)
        self.travser(root.right)
        
        
