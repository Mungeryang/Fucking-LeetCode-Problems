#longest palindrome string最长回文字符串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ' '
        for i in range(len(s)):
            start = max(0,i-len(res)-1)
            tmp = s[start : i+1]
            #分情况：s中含有字母的个数
            if tmp == tmp[::-1]:
                res = tmp
            else:
                tmp = tmp[1:]
                if tmp == tmp[::-1]:
                    res = tmp
        return res