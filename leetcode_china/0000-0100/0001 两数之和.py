"""
    编号：0001
    题目：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
    时间：2022年1月19日
"""
class Solution(object):
    @staticmethod
    def twoSum1(self, nums, target):
        """
        我的答案：列表解法
            57 / 57 个通过测试用例
            状态：通过
            执行用时: 1848 ms
            内存消耗: 13.9 MB
        :param nums: 整形数组
        :param target: 两数之和
        :return: 两数在数组中的索引
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @staticmethod
    def twoSum(self, nums, target):
        """
        参考答案：哈然表实现
            57 / 57 个通过测试用例
            状态：通过
            执行用时: 20 ms
            内存消耗: 13.8 MB
        :param nums: 整形数组
        :param target: 两数之和
        :return: 两数在数组中的索引
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []