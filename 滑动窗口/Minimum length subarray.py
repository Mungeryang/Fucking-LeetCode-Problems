#长度最小子数组
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #判断极端情况
        if len(nums) == 0:
            return 0
        #确定最值
        res = len(nums) + 1
        s = 0
        #定义双指针
        right = left = 0
        #扩大窗口
        while(right < len(nums)):
            s = s + nums[right]
            right += 1
            #比较目标值，扩大窗口的终止条件
            while s >= target:
                #righ-left为窗口内的元素
                res = min(res,right-left)
                #从左侧缩小窗口
                s = s - nums[left]
                left += 1
        #所有元素的和小于target
        if res == len(nums)+1:
            return 0
        #符合条件输出
        else:
            return res