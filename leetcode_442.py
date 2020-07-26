# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """
    给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。找到所有出现两次的元素。
    solution: 所谓的原地Hash, 每个元素换到它所对应的下标-1处, 最后不在所处的下标-1位置的元素即为出现两次的元素。
    Notes: python swap封装一个函数实现, nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] 有问题！
    """
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            while nums[i] != nums[nums[i]-1]:
                self.__swap(nums, i, nums[i]-1)
        result = []
        for i in range(length):
            if nums[i] != i+1:
                result.append(nums[i])
        return result

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]


solution = Solution()

if __name__ == "__main__":
    input = [4, 3, 2, 7, 8, 2, 3, 1]
    result = solution.findDuplicates(input)
    print(result)
