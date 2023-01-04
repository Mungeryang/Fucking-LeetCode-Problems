#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

//变量定义为全局变量之后的值是0
const int N = 10;
int n;
int state[N];
bool used[N];

void dfs(int u)
{
    //边界
    if (u > n)
    {
        for (int i = 1; i <= n; i++)
        {
            //打印方案
            printf("%d", state[i]);
        }
        puts(" ");
        return;
    }
    //依次枚举每一个分支，即当前位置可以填入哪一个数字
    for (int i = 1; i <= n; i++)
    {
        if (!used[i])
        {
            //选中位置填入数字
            state[u] = i;
            used[i] = true;
            //递归进入到下一个位置的分支
            dfs(u + 1);
            //回溯，恢复位置状态
            state[u] = 0;
            used[i] = false;
        }
    }
}

int main()
{
    scanf("%d", &n);
    dfs(1);
    system("pause");
    return 0;
}