/*
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
*/
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class Solution{
private:
    vector<vector<int>> res;//初始化结果存放
    vector<int> path;//初始化路径存放
    void backtrack(vector<int>& nums,int startIndex){
        res.push_back(path);
        if(startIndex > nums.size()){
            return;
        }
        for(int i = startIndex;i < nums.size();i++){
            path.push_back(nums[i]);
            backtrack(nums,i + 1);//递归
            path.pop_back();//回溯
        }
    }
public:
    vector<vector<int>> subsets(vector<int>& nums){
        path.clear();
        res.clear();
        backtrack(nums,0);
        return res;
    }
};

/*
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
*/
class Solution{
private:
    vector<vector<int>> res;//初始化结果存放
    vector<int> path;//初始化路径存放
    void backtrack(vector<int>& nums,int startIndex,vector<bool>& used){
        res.push_back(path);
        if(startIndex > nums.size()){
            return;
        }
        for(int i = startIndex;i < nums.size();i++){
            if(i > 0 && nums[i] == nums[i - 1] && used[i - 1] == false){
                continue;
            }
            path.push_back(nums[i]);
            used[i] = true;
            backtrack(nums,i + 1,used);//递归
            used[i] = false;
            path.pop_back();//回溯
        }
    }
public:
    vector<vector<int>> subsets(vector<int>& nums){
        vector<bool> used(nums.size(),false);
        path.clear();
        res.clear();
        sort(nums.begin(),nums.end());
        backtrack(nums,0,used);
        return res;
    }
};