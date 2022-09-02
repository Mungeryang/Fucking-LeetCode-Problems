
#include<vector>
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
    TreeNode* pur = nullptr;//记录前一个节点
    //TreeNode* cur = root;
    bool isValidBST(TreeNode* root) {
        if(root == nullptr) return true;
        //中序遍历思路
        bool left = isValidBST(root->left);
        //相当于是中序遍历操作中在操作的判断
        //运用头结点pur判断是否是一个递增的序列
        if(pur != nullptr && pur->val >= root->val) return false;
        pur = root;
        bool right = isValidBST(root->right);
        return left && right;
    }
};

class Solution {
private:
    //思路：中序遍历构建一个递增的数组
    vector<int> res;
    void travser(TreeNode* root){
        if(root == NULL) return;
        travser(root->left);
        res.push_back(root->val);
        travser(root->right);
    }
public:
    bool isValidBST(TreeNode* root) {
        res.clear();
        travser(root);
        for(int i = 1;i < res.size();i++){
            if(res[i] <= res[i - 1]){
                return false;
            }
        }
        return true;
    }
};