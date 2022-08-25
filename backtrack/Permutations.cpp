/*
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
全排列
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
*/
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<string>
#include<algorithm>
//手撸一个排列组合的回溯算法

using namespace std;

//排列可以重复的回溯函数的书写
class Solution{
private:
    vector<vector<int>> res;//初始化结果存放
    vector<int> path;//初始化路径存放
    void backtrack(vector<int>& nums,vector<bool>& used){
        if(path.size() == nums.size()){
            res.push_back(path);
            return;
        }
        for(int i = 0;i < nums.size();i++){
            path.push_back(nums[i]);
            used[i] == true;
            backtrack(nums,used);
            used[i] = false;
            path.pop_back();
        }
        
    }
public:
    vector<vector<int>> permute(vector<int>& nums){
        vector<bool> used(nums.size(),false);
        path.clear();
        res.clear();
        sort(nums.begin(),nums.end());
        backtrack(nums,used);
        return res;
    }

};
