# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        #对称二叉树的条件
        if left != None and right == None:
            return False
        elif left == None and right != None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False
        #此时就是左右节点相同进入下一层遍历
        ots = self.compare(left.left,right.right)
        ins = self.compare(left.right,right.left)
        isSymmetric = ots and ins
        return isSymmetric