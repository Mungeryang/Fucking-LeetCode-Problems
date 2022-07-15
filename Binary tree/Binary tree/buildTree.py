#前序和中序遍历结果构造二叉树
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #树为空，进行递归终止
        if not preorder:
            return None
        
        #找到并构造根节点
        rootval = preorder[0]
        root = TreeNode(rootval)
        #从中序遍历切割
        index = inorder.index(rootval)
        inleft = inorder[:index]
        inright = inorder[index + 1:]
        #重点：切割前序数组：注意子数组大小一定保持不变
        preleft = preorder[1:1+len(inleft)]
        preright = preorder[len(inleft)+1:]
        #递归
        root.left = self.buildTree(preleft,inleft)
        root.right = self.buildTree(preright,inright)
        return root

#中序与后序遍历序列构造二叉树
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        #特殊情况判断
        if not postorder:
            return None
        #找到并构建根节点
        rootval = postorder[-1]
        root = TreeNode(rootval)
        #中序数组在确定位置并切割数组
        index = inorder.index(rootval)
        inleft = inorder[:index]
        inright = inorder[index+1:]
        #重点是后序数组切割大小
        poleft = postorder[:len(inleft)]
        poright = postorder[len(inleft):len(postorder)-1]
        #递归
        root.left = self.buildTree(inleft,poleft)
        root.right = self.buildTree(inright,poright)
        return root