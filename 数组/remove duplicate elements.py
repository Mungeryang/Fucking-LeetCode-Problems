#移除重复元素
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #双指针
        slow,fast = 0,0
        while(fast < len(nums)):
            if(nums[fast] != nums[slow]):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1