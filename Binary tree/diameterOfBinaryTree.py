#最大直径
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        #定义深度函数
        def depth(node):
            #根节点
            if not root:
                return 
            #递归左子树
            L = depth(node.left)
            #递归右子树
            R = depth(node.right)
            #更新结果
            self.ans = max(self.ans,L + R + 1)
            return max(L,R) + 1
        depth(root)
        return self.ans - 1


