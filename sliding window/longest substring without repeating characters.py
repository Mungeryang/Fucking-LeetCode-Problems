class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #极端条件判断
        if len(s) == 0:
            return 0
        #定义所需变量
        left = count = res = 0
        #遍历列表的时间复杂度是O（n），遍历集合的时间复杂度是O（1）
        windows = set()
        #有指针依次向后遍历
        for i in range(len(s)):
            #计数
            count += 1
            #右指针指向元素已经在窗口中，即出现重复元素
            while s[i] in windows:
                #缩小窗口
                windows.remove(s[left])
                count -= 1
                left += 1
            #保留最值
            res = max(res,count)
            #窗口右侧加入元素
            windows.add(s[i])
        #返回结果
        return res