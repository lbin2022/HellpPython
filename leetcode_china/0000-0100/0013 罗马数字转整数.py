"""
    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

    例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

    给定一个罗马数字，将其转换成整数。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/roman-to-integer
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def romanToInt(s: str) -> int:
        dicts, res = {'MMM': 3000, 'MM': 2000, 'M': 1000, 'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600, 'D': 500, 'CD': 400,
                      'CCC': 300, 'CC': 200, 'C': 100, 'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60, 'L': 50, 'XL': 40,
                      'XXX': 30, 'XX': 20, 'X': 10, 'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6, 'V': 5, 'IV': 4,
                      'III': 3, 'II': 2, 'I': 1}, 0
        for k, v in dicts.items():
            if s.startswith(k):
                res += v
                s = s.removeprefix(k)
        return res
