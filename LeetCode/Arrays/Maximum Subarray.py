"""
53. Maximum Subarray
Easy

11697

564

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        0(n)
        Input : nums [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        Output: 6
        find maxsubarray 
        Plan:
        start looping by first index and current index, and find if totalSum max is                   maxSum + 1 or index, and return maxSum.
        Later find the max of maxIndex, and maxIndex, and return maxIndex
        """
        maxSum = maxIndex = nums[0]
        for i in range(1, len(nums)):
            maxSum = max(maxSum + nums[i], nums[i])
            maxIndex = max(maxSum, maxIndex)
        return maxIndex