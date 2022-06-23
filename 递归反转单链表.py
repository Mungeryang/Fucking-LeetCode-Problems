class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


# 将L转化为链表
def make_list(L):
    # 将L初始化为链表
    head = ListNode(L[0])
    cur = head
    for i in L[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


# 遍历链表
def print_list(head):
    cur = head
    while cur != None:
        print(cur.data, end=' ')
        cur = cur.next


# 递归法  反转链表
def reverse_list(head):
    # 三要素
    # 1.明确函数功能，该函数可以将链表反转，并返回一个头节点
    # 2.结束条件：当链表为空或只有一个节点时返回
    if head == None or head.next == None:
        return head
    # 3.等价条件（缩小范围），对于数组来讲，缩小范围是n——>n-1，对于链表来讲则可以考虑head——>head.next
    reverse = reverse_list(head.next)  # 假设reverse是head以后的、已经反转过的链表

    # 接下来要做的是将head节点接到已经反转过的reverse上
    # tmp = head.next
    # tmp.next = head
    # head.next = None

    #labuladong的递归方法
    head.next.next = head
    head.next = None
    return reverse  # 返回新的列表

# 迭代法,利用双指针进行反转
def diedai_list(head):
    reverse1 = diedai_list(head.next)
    #设置双指针
    cur = head
    por = None
    #迭代实现指针置换方向的操作时关键核心
    while cur:
        #记录最后一个结点
        tmp = cur.next
        # 改变节点的指向,反转链表
        cur.next = por
        por = cur
        # 继续处理后面的链表
        cur = tmp

    #     tmp = cur.next
    #     cur.next = por
    #     por = cur
    #     cur = tmp
    # head = por
    return reverse1



if __name__ == '__main__':
    L = [3, 2, 7, 8]
    head = make_list(L)

    # 正序打印
    print('原始list：')
    print_list(head)
    print('\n')

    # 反转后打印
    revere = reverse_list(head)
    print('反转一次的list：')
    print_list(revere)
    print('\n')

    # 反转后打印
    revere1 = diedai_list(head)
    print('反转二次的list：')
    print_list(revere1)
    print('\n')











