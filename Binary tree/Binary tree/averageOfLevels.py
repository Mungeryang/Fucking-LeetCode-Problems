#计算二叉树每层节点的平均数
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        #保存结果
        res = []
        ans = []
        #定义层序遍历函数
        def cengxu(root,depth):
            if not root:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            #遍历左右子树
            if root.left:
                cengxu(root.left,depth + 1)
            if root.right:
                cengxu(root.right,depth + 1)
        cengxu(root,0)
        for i in range(len(res)):
            sum1 = sum(res[i])
            num = len(res[i])
            ans.append(sum1 / num)
        return ans