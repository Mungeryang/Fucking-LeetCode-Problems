#判断单链表是否包含环并找出环起点

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        #寻找中点的套路
        while(fast != None and fast.next != None):
            #快指针前进两步
            fast = head.next.next
            #慢指针前进一步
            slow = head.next
            #当快指针比慢指针多走一圈时，相遇便成环
            if(fast == slow):
                return True
        return False
#不知道为啥这个代码总是运行超时，是时间复杂度太大吗？-2022.06.21

#判断两个单链表是否相交并找出交点
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            #p1 走一步，如果走到 A 链表末尾，转到 B 链表
            if(p1 == None):
                p1 = headB
            else:
                p1 = p1.next
            #p2 走一步，如果走到 B 链表末尾，转到 A 链表
            if(p2 == None):
                p2 = headA
            else:
                p2 = p2.next
        return p1