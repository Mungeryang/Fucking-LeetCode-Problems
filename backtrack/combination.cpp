/*
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<string>
//手撸一个排列组合的回溯算法

using namespace std;

//排列可以重复的回溯函数的书写
class Solution{
private:
    vector<vector<int>> res;//初始化结果存放
    vector<int> path;//初始化路径存放
    void backtrack(vector<int>& candidates,int target,int sum,int startIndex){
        //终止条件
        if(sum > target){
            return;
        }
        if(sum == target){
            res.push_back(path);
            return;
        }
        for(int i = startIndex; i < candidates.size();i++){
            sum += candidates[i];
            path.push_back(candidates[i]);
            //可以从自身开始计数，所以无需i + 1
            backtrack(candidates,target,sum,i);//递归纵向深处遍历
            sum -= candidates[i];//回溯
            path.pop_back();//回溯
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates,int target){
        path.clear();
        res.clear();
        backtrack(candidates,target,0,0);
        return res;
    }

};

/*
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
class Solution
{
private:
    /* data */
    vector<vector<int>> res;//初始化结果存放
    vector<int> path;//初始化路径存放
    void backtrack(vector<int>& candidates,int target,int sum,int startIndex,vector<bool>& used){
        if(sum > target){
            return;
        }
        if(sum == target){
            res.push_back(path);
            return;
        }
        for(int i = startIndex;i < candidates.size();i++){
            if(i > 0 && candidates[i] == candidates[i - 1] && used[i - 1] == false){
                continue;
            }
            sum += candidates[i];
            path.push_back(candidates[i]);
            used[i] = true;
            backtrack(candidates,target,sum,i + 1,used);
            used[i] == false;//回溯
            sum -= candidates[i];//回溯
            path.pop_back();

        }
    }
public:
    
};


