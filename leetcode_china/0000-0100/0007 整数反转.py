"""
    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
    如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-integer
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:
    @staticmethod
    def reverse(self, x: int) -> int:
        """
        执行结果：        通过
        执行用时：        32 ms        , 在所有 Python3 提交中击败了        81.10%        的用户
        内存消耗：        14.9 MB        , 在所有 Python3 提交中击败了        78.45%        的用户
        通过测试用例：        1032 / 1032
        """
        if x == 0:
            return x
        flag = x // abs(x)
        str_x = str(abs(x)).strip('0')
        res = int(str_x[::-1]) * flag
        if 2 ** 31 - 1 > res > - (2 ** 31):
            res = 0

        return res
