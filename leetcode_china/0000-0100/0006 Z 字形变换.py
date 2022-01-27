"""
    将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
    比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
    P   A   H   N
    A P L S I I G
    Y   I   R
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/zigzag-conversion
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        """
        1157 / 1157 个通过测试用例
        状态：通过
        执行用时: 52 ms
        内存消耗: 15.3 MB
        """
        len_s, circle_num, half_num = len(s), 2 * numRows - 2, numRows - 1
        if len_s < 3 or numRows == 1:
            return s
        directory = ['down' if index % circle_num < half_num else 'up' for index in range(len_s)]
        res_list, cur, res = ['' for i in range(numRows)], 0, ''
        for i in range(len_s):
            res_list[cur] += s[i]
            if directory[i] == 'down':
                cur += 1
            else:
                cur -= 1
        for s in res_list:
            res += s
        return res


units = {'a':'a', 'ab':'ab', 'abc':'abc', 'abcd':'abdc', 'abcde':'aebdc', 'abcdef':'aebdfc', 'PAYPALISHIRING':'PINALSIGYAHIPI'}
for k, v in units.items():
    print('units: {} expect: {} real:{}'.format(str(k).ljust(15, ' '), str(v).ljust(15, ' '), Solution.convert(k, 1)))
