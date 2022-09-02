/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:

    int ret = INT_MIN;
    //函数定义和返回值是什么？
    // 定义：计算从根节点 root 为起点的最大单边路径和
    int dfs(TreeNode* root){
        //终止条件
        if(root == NULL){
            return 0;
        }
        int leftsum = max(0,dfs(root->left));
        int rightsum = max(0,dfs(root->right));
        // 后序遍历位置，顺便更新最大路径和
        int pathsum = root->val + leftsum + rightsum;
        ret = max(ret,pathsum);
        // 实现函数定义，左右子树的最大单边路径和加上根节点的值
        // 就是从根节点 root 为起点的最大单边路径和
        return max(leftsum,rightsum) + root->val;

    }
public:
    int maxPathSum(TreeNode* root) {
        if(root == NULL){
            return 0;
        }
        dfs(root);
        return ret;

    }
};