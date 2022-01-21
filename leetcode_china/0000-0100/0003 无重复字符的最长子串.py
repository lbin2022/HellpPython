"""
    编号：0003
    题目：给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
    时间：2022年1月21日
"""
import datetime


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        我的答案：列表实现
            986 / 987 个通过测试用例
        :param s: 字符串
        :return: 不重复子串长度
        """
        len_s = len(s)
        for l_sub in range(len_s, 0, -1):
            for start_pos in range(0, len_s - l_sub + 1):
                sub = s[start_pos:start_pos + l_sub]
                sub_set = set(sub)
                if len(sub) == len(sub_set):
                    return l_sub

        return 0


st = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''
start = datetime.datetime.now()
print(Solution.lengthOfLongestSubstring(st))
end = datetime.datetime.now()
print('耗时', end - start)
