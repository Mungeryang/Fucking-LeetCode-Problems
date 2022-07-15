class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #老套路，设置快慢指针
        slow=0
        fast=0
        #核心代码区，区分不同目标值的设置
        while(fast <len(nums)):
            if(nums[fast] != 0):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        #与前面题唯一的不同点，是将数组去重后尾部元素修改为0，此处我用的for循环，有其他新方法欢迎大佬们修改提出意见
        for i in range(slow,len(nums)):
            nums[i] = 0