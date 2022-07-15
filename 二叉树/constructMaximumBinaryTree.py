# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums) :
        #根节点的判断
        if not root:
            return None
        #找到数组中的最大值与其对应的索引
        maxval = max(nums)
        index = nums.index(maxval)
        #将最大值构造为树的头结点
        root = TreeNode(maxval)
        #构造左右子树(切片操作)
        left = nums[:index]
        right = nums[index + 1:]
        #递归遍历
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root

        
        