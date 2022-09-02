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
    int res = 0;
    //遍历函数时什么、返回值是什么？
    int dfs(TreeNode* root,int parentVal){
        //终止条件
        if(root == NULL){
            return 0;
        }
        // 利用函数定义，计算左右子树值为 root.val 的最长树枝长度
        int left = dfs(root->left,root->val);
        int right = dfs(root->right,root->val);

        //后序操作:直接返回左右子树最大路径之和
        res = max(res, left + right);
        // 如果 root 本身和上级值不同，那么整棵子树都不可能有同值树枝
        if(root->val != parentVal){
            //注意返回值的设定
            return 0;
        }
        // 实现函数的定义：
        // 以 root 为根的二叉树从 root 开始值为 parentVal 的最长树枝长度
        // 等于左右子树的最长树枝长度的最大值加上 root 节点本身
        return 1 + max(left,right);


    }
public:
    int longestUnivaluePath(TreeNode* root) {
        if(root == NULL){
            return 0;
        }
        dfs(root,root->val);
        return res;

    }
};