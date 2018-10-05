"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0] * len(nums) 

        for i in range(len(nums)-1, -1, -1):
            tmp = [0]
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    tmp.append(l[j])
            l[i] = 1 + max(tmp)
         
        return max(l) if l else 0