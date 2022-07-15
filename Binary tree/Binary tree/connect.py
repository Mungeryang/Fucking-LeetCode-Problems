"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#填充每个节点的下一个右侧节点指针
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #根节点情况
        if root == None:
            return
        self.traverse(root.left,root.right)
        return root
    def traverse(self,node1,node2):
        if node1 == None and node2 == None:
            return
        #连接传入的两个节点
        node1.next = node2
        #前序遍历
        self.traverse(node1.left,node1.right)
        self.traverse(node2.left,node2.right)
        self.traverse(node1.right,node2.left)