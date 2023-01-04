#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

const int N = 15;

int n;
//状态数组，记录每个位置当前的状态：
// 0表示还没考虑，1表示选他，2表示不选他
int st[N];

// u表示当前操作的位数
void dfs(int u)
{
    // u > n表示:每个分支孩子节点的边界条件
    if (u > n)
    {
        for (int i = 1; i <= n; i++)
        {
            if (st[i] == 1)
            {
                printf("%d", i);
            }
        }
        printf("\n");
        return;
    }
    //针对每一个分支节点的递归
    st[u] = 2;
    dfs(u + 1); //第一个分支：不选
    st[u] = 0;  //恢复现场，以便后面回溯

    st[u] = 1;
    dfs(u + 1); //第二个分支：选
    st[u] = 0;  //恢复现场，以便后面回溯
}

int main()
{
    cin >> n;
    dfs(1);
    system("pause");
    return 0;
}