#乘积小于K的子数组
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #特殊情况
        if k <= 1:
            return 0
        #双指针
        left = 0
        right = 0
        #记录器与计数器
        res = 1
        result = 0
        #扩大窗口
        while right < len(nums):
            res *= nums[right]
            #缩小窗口
            while res >= k:
                res /= nums[left]
                left += 1
            result += (right-left+1)
            right += 1
        return result