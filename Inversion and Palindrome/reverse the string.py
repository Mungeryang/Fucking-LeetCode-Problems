#反转字符串
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        # 该方法已经不需要判断奇偶数，经测试后时间空间复杂度比用 for i in range(right//2)更低
        # 推荐该写法，更加通俗易懂
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1