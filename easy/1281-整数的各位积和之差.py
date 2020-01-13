#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author：Elvira

"""
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

示例 1：
输入：n = 234
输出：15
解释：
各位数之积 = 2 * 3 * 4 = 24
各位数之和 = 2 + 3 + 4 = 9
结果 = 24 - 9 = 15

示例 2：
输入：n = 4421
输出：21
解释：
各位数之积 = 4 * 4 * 2 * 1 = 32
各位数之和 = 4 + 4 + 2 + 1 = 11
结果 = 32 - 11 = 21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import reduce


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n)) == 1:
            return 0
        return reduce(lambda x, y: int(x) * int(y), list(str(n))) - sum(map(int, list(str(n))))


if __name__ == '__main__':
    s = Solution()
    nums = 1
    res = s.subtractProductAndSum(nums)
    print(res)
