#数组中移除元素
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #双指针
        slow,fast = 0,0
        while(fast < len(nums)):
            if(nums[fast] != val):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow