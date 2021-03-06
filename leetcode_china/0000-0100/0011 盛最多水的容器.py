"""
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

    说明：你不能倾斜容器。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/container-with-most-water
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxArea(height: List[int]) -> int:
        """ 暴力枚举　"""
        len_h = len(height)
        if len_h < 2:
            return 0
        res = 0
        for i in range(len_h - 1):
            for j in range(i + 1, len_h):
                new = (j - i) * min(height[i], height[j])
                if res < new:
                    res = new
        return res

    def maxArea2(height: List[int]) -> int:
        """ 双指针，短边内移　"""
        left, right, res = 0, len(height), 0
        while left < right:
            res = max(res, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right += 1
        return res
