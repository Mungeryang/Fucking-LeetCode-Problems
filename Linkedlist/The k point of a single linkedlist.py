#先利用for循环让快指针先走k步，在利用上题寻找中点思路即可解决
#寻找倒数第k个节点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        #先让快指针fast向前走k步
        for i in range(k):
            fast = fast.next
        #while(fast != None and fast.next != None)多加一个fast的next的结果为[3,4,5]与原题结果不符合;注意条件控制
        while(fast != None):
            slow = slow.next
            fast = fast.next
        return slow