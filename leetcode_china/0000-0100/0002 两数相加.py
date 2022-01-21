"""
    编号：0002
    题目：给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
            请你将两个数相加，并以相同形式返回一个表示和的链表。
            你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
            链接：https://leetcode-cn.com/problems/add-two-numbers
    时间：2022年1月20日
"""


class ListNode:
    """ Definition for singly-linked list. """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            v = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            cur.next = ListNode(v)
            cur = cur.next

        return head.next
