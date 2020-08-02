# -*- coding: utf-8 -*-
from itertools import zip_longest


class Solution:
    """
    给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
    输入：S = "ab#c", T = "ad#c"
    输出：true
    解释：S 和 T 都会变成 “ac”。
    Notes: 倒序指针取字符, 注意python yield和zip_longest的用法
    """
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_real_string(temp):
            backspace = 0
            for ch in reversed(temp):
                if ch == "#":
                    backspace += 1
                elif backspace:
                    backspace -= 1
                else:
                    yield ch
        return all(x == y for x, y in zip_longest(get_real_string(S), get_real_string(T)))


solution = Solution()
if __name__ == "__main__":
    s1 = "ab#c"
    s2 = 'ad#c'
    result = solution.backspaceCompare(s1, s2)
    print(result)
