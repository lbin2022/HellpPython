"""
    编号：0005
    题目：给你一个字符串 s，找到 s 中最长的回文子串。
    时间：2022年1月23日
"""


class Solution:
    @staticmethod
    def longestPalindrome0(s: str) -> str:
        """
        180 / 180 个通过测试用例
        状态：通过
        执行用时: 5608 ms
        内存消耗: 15 MB
        """
        len_str = len(s)
        for length in range(len_str, 0, -1):
            for start in range(len_str - length + 1):
                res = s[start:start+length]
                if res == res[::-1]:
                    return res


units: dict = {'d':'d', 'dd':'dd', 'ddad':'dad', 'dbabd':'dbabd', 'dadad':'dad', 'abcb':'bcb', 'aabcbaa':'aabcbaa',
               'bcbcb':'bcbcb'}
for k, v in units.items():
    print('units: {} with expect result: {} and read result:{}'.format(str(k).ljust(15, ' '), str(v).ljust(15, ' '),
                                                                       Solution.longestPalindrome0(k)))
