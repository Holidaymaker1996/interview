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


# 数组先升序再降序，找前后相同？
def same(list):
    n = len(list)
    count = 0
    p, q = 0, n - 1
    for i in range(n-1):
        if list[i] == list[i+1]:
            a = i
            break
        if list[i] > list[i+1]:
            a = i
            break
    print(a, 'a')
    for i in range(len(list)-1):
        print(list[i], '进入循环')
        if i == a:
            break
        if list[p] == list[q]:
            count += 1
            print(list[p], '相等')
            p += 1
            q -= 1
        if list[p] < list[q]:
            print('p', list[p], 'q', list[q], '小于')
            p += 1
            # i -= 1
        if list[p] > list[q]:
            print('p', list[p], 'q', list[q], '大于')
            q -= 1
            # i -= 1
    print(count)
    return count

if __name__ == '__main__':
    # lengthOfLongestSubstring("abcabcda")
    # s = 'ac'
    # demo(s)
    # prime(3, 10000)
    list = [1, 2, 3, 4, 3, 2]
    same(list)



# 海量数据处理 - 10亿个数中找出最大的10000个数（top K问题）
# https://www.cnblogs.com/itxiaok/p/10385676.html
# https://www.nowcoder.com/tutorial/93/2f895548adc24f0b88ffcb01c7973f23
# 1、直接全部排序（只适用于内存够的情况）
# 当数据量较小的情况下，内存中可以容纳所有数据。则最简单也是最容易想到的方法是将数据全部排序，然后取排序后的数据中的前K个。
# 这种方法对数据量比较敏感，当数据量较大的情况下，内存不能完全容纳全部数据，这种方法便不适应了。即使内存能够满足要求，
# 该方法将全部数据都排序了，而题目只要求找出top K个数据，所以该方法并不十分高效，不建议使用。
#
# 2、快速排序的变形 （只使用于内存够的情况）
# 这是一个基于快速排序的变形，因为第一种方法中说到将所有元素都排序并不十分高效，只需要找出前K个最大的就行。
# 这种方法类似于快速排序，首先选择一个划分元，将比这个划分元大的元素放到它的前面，比划分元小的元素放到它的后面，
# 此时完成了一趟排序。如果此时这个划分元的序号index刚好等于K，那么这个划分元以及它左边的数，刚好就是前K个最大的元素；
# 如果index  > K，那么前K大的数据在index的左边，那么就继续递归的从index-1个数中进行一趟排序；
# 如果index < K，那么再从划分元的右边继续进行排序，直到找到序号index刚好等于K为止。
# 再将前K个数进行排序后，返回Top K个元素。这种方法就避免了对除了Top K个元素以外的数据进行排序所带来的不必要的开销。
#
# 3、最小堆法
# 这是一种局部淘汰法。先读取前K个数，建立一个最小堆。然后将剩余的所有数字依次与最小堆的堆顶进行比较，如果小于或等于堆顶数据，
# 则继续比较下一个；否则，删除堆顶元素，并将新数据插入堆中，重新调整最小堆。当遍历完全部数据后，最小堆中的数据即为最大的K个数。
#
# 4、分治法
# 将全部数据分成N份，前提是每份的数据都可以读到内存中进行处理，找到每份数据中最大的K个数。此时剩下N*K个数据，
# 如果内存不能容纳N*K个数据，则再继续分治处理，分成M份，找出每份数据中最大的K个数，如果M*K个数仍然不能读到内存中，
# 则继续分治处理。直到剩余的数可以读入内存中，那么可以对这些数使用快速排序的变形或者归并排序进行处理。
#
# 5、Hash法
# 如果这些数据中有很多重复的数据，可以先通过hash法，把重复的数去掉。这样如果重复率很高的话，会减少很大的内存用量，
# 从而缩小运算空间。处理后的数据如果能够读入内存，则可以直接排序；否则可以使用分治法或者最小堆法来处理数据。