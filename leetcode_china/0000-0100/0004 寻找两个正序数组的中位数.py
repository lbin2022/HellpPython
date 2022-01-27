"""
    编号：0004
    题目：给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
        算法的时间复杂度应该为 O(log (m+n)) 。
    时间：2022年1月22日
"""
import math
from typing import List


class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        """
        2094 / 2094 个通过测试用例
        状态：通过
        执行用时: 36 ms
        """
        res = sorted(nums1 + nums2)
        n = len(res)
        mid = n // 2
        return (res[mid - 1] + res[mid]) / 2 if n % 2 == 0 else res[mid]



    def findMedianSortedArrays0(self, nums1: List[int], nums2: List[int]) -> float:
        """
        2094 / 2094 个通过测试用例
        状态：通过
        执行用时: 44 ms
        内存消耗: 15.2 MB
        """
        res = nums1 + nums2
        res = sorted(res)
        n = len(res)
        left = (n-1)//2
        right = math.ceil((n-1)/2)
        oo = n % 2
        if oo == 0:
            res = (res[left] + res[right]) / 2
        else:
            res = res[left]
        return res