# -*- coding: utf-8 -*-
from typing import List


class Solution:
    """
        给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
        说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
        Solution 摩尔投票法, 超过n/3的元素只能有两个
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        a, b = 0, 0
        count_a, count_b = 0, 0
        for tmp in nums:
            if tmp == a:
                count_a += 1
                continue
            if tmp == b:
                count_b += 1
                continue
            if count_a == 0:
                a = tmp
                count_a += 1
                continue
            if count_b == 0:
                b = tmp
                count_b += 1
                continue
            count_a -= 1
            count_b -= 1

        print(a, b, count_a, count_b)
        count_a = sum([1 for _ in nums if _ == a])
        count_b = sum([1 for _ in nums if _ == b])
        if count_a > len(nums)/3:
            result.append(a)
        if count_b > len(nums)/3 and a != b:
            result.append(b)
        return result

    def majorityElement_myself(self, nums: List[int]) -> List[int]:
        result = []
        if not nums:
            return result
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and nums[j] != nums[i]:
                j = j + 1
            # print(i, j)
            if j < len(nums) and i + 1 < len(nums):
                self._swap(nums, i+1, j)
        # print(nums)
        count = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] == nums[i]:
                count += 1
            else:
                if count > len(nums)/3:
                    result.append(nums[i])
                count = 1
        if count > len(nums)/3:
            result.append(nums[-1])
        return result

    def _swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


solution = Solution()
if __name__ == "__main__":
    input = [0, 0, 0]
    result = solution.majorityElement(input)
    print(result)
