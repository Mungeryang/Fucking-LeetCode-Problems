# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #分解问题后序遍历
        if root == None:
            return
        #递归左右子树
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        #后序操作;交换节点
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root

#遍历思路
class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.travser(root)
        return root
    #遍历函数书写
    def travser(self,root):
        #根节点判断
        if root == None:
            return
        #前序操作
        tmp = root.left
        root.left = root.right
        root.right = tmp
        #递归遍历
        self.travser(root.left)
        self.travser(root.right)
