#include<iostream>
#include<queue>
#include<stdlib.h>
#include<vector>

using namespace std;

struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int BFS(TreeNode * root){
    if(root == NULL) return 0;  //终止条件判断
    queue<TreeNode*> que;   //创建队列
    que.push(root); //将根节点入队
    int sum = 0;//设置记录信号
    while(!que.empty()){
        sum = 0;//每次循环之前归零，记录单层的和
        int sz = que.size();//求出队列长度
        for(int i = 0;i < sz;i++){
            //for循环依次对每层求和
            TreeNode* cur = que.front();//取对头元素为初始指针节点
            que.pop();
            sum += cur->val;
            if(cur->left != NULL){
                cur = cur->left;
            }
            if(cur->right != NULL){
                cur = cur->right;
            }


        }

    }
    return sum;



}