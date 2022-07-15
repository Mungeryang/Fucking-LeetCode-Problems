# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
            
        #递归左右子树
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right) # 右
        
        cur_val = 0
        if root.left and not root.left.left and not root.left.right: 
            cur_val = root.left.val  # 中
            
        return cur_val + left_left_leaves_sum + right_left_leaves_sum