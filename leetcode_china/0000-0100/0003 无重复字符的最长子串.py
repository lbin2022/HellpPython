"""
    编号：0003
    题目：给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
    时间：2022年1月21日
"""
import datetime


class Solution:
    @staticmethod
    def lengthOfLongestSubstring1(s: str) -> int:
        """
        我的答案：列表实现
        :param s: 字符串
        :return: 不重复子串长度
        """
        str_result = str_cur = s[0]   # 结果字符串, 当前子串
        str_max = len(s)
        result_max = len(set(s))    # 可能的最大结果
        if result_max == str_max:   # 无重复，直接返回s
            str_result = s
        else:
            for i in range(1, str_max):
                if str_cur.find(s[i]) < 0:
                    str_cur += s[i]
                    if len(str_result) < len(str_cur) <= result_max:
                        str_result = str_cur
                else:
                    str_cur = str_cur[1:] + s[i]
        return len(str_result)

    @staticmethod
    def lengthOfLongestSubstring0(s: str) -> int:
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


st = '''"pwwkew"'''
start = datetime.datetime.now()
print(Solution.lengthOfLongestSubstring1(st))
print(Solution.lengthOfLongestSubstring0(st))
end = datetime.datetime.now()
print('耗时', end - start)
