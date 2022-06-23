# class ListNode:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
#
def make_list(L):
    head = Node(L[0])
    cur = head
    for i in L[1:]:
        cur.next = Node(i)
        cur = cur.next

    return head
#
# 遍历链表
def print_list(head):
    cur = head
    while cur != None:
        print(cur.data, end='->')
        cur = cur.next
#
# #递归反转单链表
# def reserve(head):
#     if (head == None and head.next == None):
#         return None
#     last = reserve(head.next)
#     head.next.next = head
#     head.next = None
#     return last

class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


def reverseList(head):
    if head == None or head.next == None:  # 若链表为空或者仅一个数就直接返回
        return head
    pre = None
    next = None
    while (head != None):
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


if __name__ == '__main__':
    L = [3,2,5,6]
    head = make_list(L)
    re = reverseList(head)
    print(re.elem,re.next.elem,re.next.next.elem,re.next.next.next.elem)










