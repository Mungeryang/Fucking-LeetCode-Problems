# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#递归解法
from turtle import right


class Solution:
    def preorderTraversal(self, root):
        def prenode(root):
            #根节点判断
            if not root:
                return
            #res = []
            #前序遍历顺序
            res.append(root.val)
            prenode(root.left)
            prenode(root.right)
        #创建空列表
        res = []
        #调用前序遍历函数
        prenode(root)
        return res


        

            
