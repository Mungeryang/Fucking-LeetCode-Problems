#层序遍历递归法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def cengxu(root,depth):
            if not root:
                return []
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                cengxu(root.left,depth+1)
            if root.right:
                cengxu(root.right,depth+1)
        cengxu(root,0)
        return res
   
#[[3],[9,20],[15,7]]最后的结果是列表的嵌套

#自底向上层序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        #记录结果
        res = []
        #定义层序遍历函数
        def cengxu(root,depth):
            #根节点判断
            if not root:
                return None
            #一开始很不理解这一步
            #观察结果:[[15,7],[9,20],[3]]；涉及到列表的嵌套
            #每当深度加一,就要增加一个子列表
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            if root.left:
                cengxu(root.left,depth + 1)
            if root.right:
                cengxu(root.right,depth + 1)
        cengxu(root,0)
        return res[::-1]