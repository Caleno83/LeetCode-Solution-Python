"""
1. Two Sum
Easy

20605

723

Add to List

Share
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force 0(n2)
        # # get i in array
        #  for i in range(len(nums)):
        #         #get second i in array
        #     for j in range(i +1, len(nums)):
        #         # if first i + second i are equal to target
        #         if nums[i] + nums[j] == target:
        #             #return first and second i
        #             return [i, j]

        # Better Solution 0(n)
        # create a dict 
        val = dict()
        # loop array with i, and num
        for i, num in enumerate(nums):
        # get difference between target - num in array
            diff = target - num
            #check if diff is in dict
            if diff in val:
                #if it is, return indexes of diff in dict
                return [val[diff], i]
            # if not return i of value
            else:
                val[num] = i 