
//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    //确定递归函数和参数设置
    TreeNode* searchBST(TreeNode* root, int val) {
        //终止条件
        if(root == nullptr || root->val == val) return root;
        //因为二叉搜索树的节点大小是有规律的所以可以简化搜索
        if(root->val > val) return searchBST(root->left,val);
        if(root->val < val) return searchBST(root->right,val);
        return nullptr; 

    }
};