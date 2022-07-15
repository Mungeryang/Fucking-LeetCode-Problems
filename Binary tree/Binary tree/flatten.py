#二叉树展开为链表
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        #根节点操作
        if root == None:
            return 
        #拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        #后序操作:分别将子树拉平为链表
        l = root.left
        r = root.right
        #将左子树作为右子树
        root.left = None
        root.right = l
        #将原先的右子树接到当前右子树的末端
        p = root
        while(p.right != None):
            p = p.right
        p.right = r