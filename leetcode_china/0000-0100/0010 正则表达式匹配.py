"""
    给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素
    所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/regular-expression-matching
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isMatch(s: str, p: str) -> bool:
        ps, pl = tuple(s), tuple(p)
        next, max, res = 0, len(pl), False
        for psi in ps:
            if next == max: return False
            pli = pl[next]
            if psi == pli or pli == '.':
                next += 1
            elif pli == '*':
                continue
            else:
                return False
        else:
            res = True
        return res


ssb = (('aa', 'a', False), ('aa', 'a.', True), ('aa', '*', True),
       ('abb', 'a', False), ('abb', 'ab.', True), ('abb', 'ab*', True), ('abb', 'a*', True), ('abb', '*', True),
       ('abc', 'abc', True), ('abc', 'a*', True), ('abc', '*', True), ('abc', '..*', True), ('abc', 'b*', False),)
for t in ssb:
    print(t[0].rjust(20, '-'), end='   ')
    print(t[1].rjust(20, '-'), end='   ')
    print(str(t[2]).rjust(20, '-'), end='   ')
    print(Solution.isMatch(t[0], t[1]))
