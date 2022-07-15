# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #结果记录
        res = []
        #定义层序遍历函数
        def cengxu(root,depth):
            if not root:
                return None
            if len(res) == depth:
                res.append(root.val)
            #res[depth].append(root.val)
            #只去遍历右子树-准确来说是去遍历每个节点的右子树
            if root.right:
                cengxu(root.right,depth + 1)
            if root.left:
                cengxu(root.left,depth + 1)
        cengxu(root,0)
        return res