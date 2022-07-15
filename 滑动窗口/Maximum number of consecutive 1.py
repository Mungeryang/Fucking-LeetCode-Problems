#连续大于1的个数
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #设置双指针
        left = 0
        right = 0
        #记录器和计数器
        res = 0
        count = 0
        while right < len(nums):
            #扩大窗口
            if nums[right] == 0:
                count += 1
            right += 1
            #缩小窗口
            if count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res,right - left)
        return res