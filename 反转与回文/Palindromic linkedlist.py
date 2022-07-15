#单链表设计
class Solution:
    def isPalindrome(self, head) -> bool:
        length = 0
        tmp = head
        while tmp: #求链表长度
            length += 1
            tmp = tmp.next
        
        result = [0] * length
        tmp = head
        index = 0
        while tmp: #链表元素加入数组
            result[index] = tmp.val
            index += 1
            tmp = tmp.next
        
        i, j = 0, length - 1
        while i < j: # 判断回文
            if result[i] != result[j]:
                return False
            i += 1
            j -= 1
        return True
        
#反转后半部分链表
class Solution:
    def isPalindrome(self, head) -> bool:
        if head == None or head.next == None:
            return True
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = None # 分割链表
        cur1 = head # 前半部分
        cur2 = self.reverseList(slow) # 反转后半部分，总链表长度如果是奇数，cur2比cur1多一个节点
        while cur1:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

    def reverseList(self, head) :
        cur = head   
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下cur的下一个节点
            cur.next = pre # 反转
            pre = cur
            cur = temp
        return pre
