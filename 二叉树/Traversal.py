#二叉树的前中后序遍历

#前序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #保存结果
        res = []

        #定义遍历函数
        def traversal(root):
            #根节点判断
            if root == None:
                return
            #前序操作
            res.append(root.val)
            #先存根节点后遍历操作
            traversal(root.left)
            traversal(root.right)
        #从主根节点开始判断
        traversal(root)
        return res


#中序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #保存结果
        res = []

        def traervsal(root):
            #根节点判断
            if root == None:
                return
            #递归遍历
            traervsal(root.left)
            #中序操作的位置
            res.append(root.val)
            traervsal(root.right)
        #从主根节点开始判断   
        traervsal(root)
        return res


#后序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #保存结果
        res = []

        #定义遍历函数
        def traversal(root):
            if root == None:
                return
            #先遍历左右子树
            traversal(root.left)
            traversal(root.right)
            #后序操作保存根节点
            res.append(root.val)
        #从主根节点开始判断
        traversal(root)
        return res
    
#主要解决遍历函数即可完成二叉树的遍历
#会写遍历函数
