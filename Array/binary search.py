#寻找一个数
'''
二分查找关键是要明确搜索区间： 1.左闭右开while(left < right) 2.左闭右闭while(left <= right)
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1 #易错点
        while(left <= right):
            mid = left + (right - left)/2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                #对于mid的操作时二分查找的一个难点。
                left = mid + 1
            elif(nums[mid] > target):
                right = mid - 1
        return -1