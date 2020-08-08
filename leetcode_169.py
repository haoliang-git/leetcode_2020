# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """
    给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
    Solution: 大于n/2的元素只有一个, map方法o(n), o(n) 排序法o(nlogn), 投票法 o(n), o(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        result = None
        count = 0
        for tmp in nums:
            print(result, count)
            if tmp == result:
                count += 1
                continue
            if count == 0:
                result = tmp
                count += 1
                continue
            count -= 1
        count = sum([1 for _ in nums if _ == result])
        if count > len(nums)/2:
            return result
        else:
            return None

    def majorityElement_ans(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

solution = Solution()
if __name__ == "__main__":
    input = [0,0,2,2]
    result = solution.majorityElement(input)
    print(result)
