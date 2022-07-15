# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = ''
        res = []
        if not root:
            return res
        self.road(root,path,res)
        return res

    #定义遍历函数 
    def road(self,cur,path,res):
        #路径表示
        path += str(cur.val)
        #叶子结点判断
        if not cur.left and not cur.right:
            res.append(path)
        #递归左右子树
        if cur.left:
            self.road(cur.left,path + '->',res)
        if cur.right:
            self.road(cur.right,path + '->',res)