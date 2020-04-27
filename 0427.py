# 1.给定一个字符串，找到最长子字符串的长度，要求子字符串中所有字符不重复
# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: 满足条件的最长子字符串为 "abc", 长度为3.
# 滑动窗口


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            print('s[{}]:{},st[{}]:{}'.format(j, s[j], s[j], st[s[j]]))
            i = max(st[s[j]], i)
            print(i)
        print(j, i)
        print('ans:{},j-i+1:{}'.format(ans, j - i + 1))
        ans = max(ans, j - i + 1)
        print('ans:{}'.format(ans))
        st[s[j]] = j + 1
        print('st[{}]:{}'.format(s[j], st[s[j]]))
        print(st)
    print(ans)
    return ans


def demo(s):
    left, ans = 0, 0
    lst = {}
    # 设置list作为索引记录当前窗口中字符串位置
    for i in range(len(s)):
        if s[i] in lst:
            left = max(left, lst[s[i]])
    # 更新新窗口中左边起始位置
        ans = max(ans, i - left + 1)
        lst[s[i]] = i + 1
    # 更新索引中重复字符位置为最新位置+1
    # +1原因是ans中i-left+1包括了首尾两项,保持一致
    print(ans)
    return ans


# 2.输入M、N，1 < M < N <1000000，求区间[M,N]内的所有素数的个数。
# 素数定义：除了1以外，只能被1和自己整除的自然数称为素数
# 输入描述: 两个整数M，N
# 输出描述: 区间内素数的个数
import math


def prime(m, n):
    prime_list = []
    for i in range(m, n+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    print(len(prime_list))
    for k in range(len(prime_list)):
        print(prime_list[k], end=" ")
        if (k + 1) % 10 == 0:
            print("\n")
    return len(prime_list)


# 3.将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(None)
        node = new_head
        while l1 and l2:
            if l1.val > l2.val:
                node.next, l2 = l2, l2.next
            else:
                node.next, l1 = l1, l1.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return new_head.next


# 去除其中的重复元素
def mergeTwoLists2(l1, l2):
    res = ListNode(None)
    node = res
    while l1 and l2:
        if l1.val < l2.val:
            node.next, l1 = l1, l1.next
        elif l1.val > l2.val:
            node.next, l2 = l2, l2.next
        else:
            node.next, l1, l2 = l1, l1.next, l2.next
        node = node.next
    if l1:
        node.next = l1
    else:
        node.next = l2
    return res.next




if __name__ == '__main__':
    # lengthOfLongestSubstring("abcabcda")
    # s = 'ac'
    # demo(s)
    prime(3, 10000)