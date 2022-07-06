#反转整数
class Solution:
    def reverse(self, x: int) -> int:
        if(x == 0):
            return 0
        if(x > 0):
            y = int(str(x)[::-1])
            return y if -2147483648<y<2147483647 else 0 
        if(x < 0):
            y = -int(str(abs(x))[::-1])
            return y if -2147483648<y<2147483647 else 0