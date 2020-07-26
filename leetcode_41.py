# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """
    给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
    Solution: 所谓的原地Hash, 每个不超过len大小的元素交换到下标-1的位置, 最后第一个不在的就是没有出现的最小正整数
              如果在len大小范围内都在自己对应的位置，那么没有出现的最小正整数为len+1
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # print(nums, i, nums[i]-1)
                self.__swap(nums, i, nums[i] - 1)
                # print(nums)
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1

    def __swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]


solution = Solution()

if __name__ == "__main__":
    input = [1, 2, 0]
    # input = [3, 4, -1, 1]
    # input = [7, 8, 9]
    # input = [-1]  #边界
    # input = [] #边界
    result = solution.firstMissingPositive(input)
    print(result)