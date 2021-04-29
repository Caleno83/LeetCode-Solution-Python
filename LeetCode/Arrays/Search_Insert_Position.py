"""
35. Search Insert Position
Easy

3451

293

Add to List

Share
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       #  # 0(n)
       # # start count with 0
       #  index = 0
       #  #for loop array nums
       #  for i in range(len(nums)):
       #      #if target is equal to index of num
       #      if target == nums[i]:
       #          #return index
       #          return i
       #      #if target is bigger than index of num
       #      elif target > nums[i]:
       #          #increment index
       #          index = i + 1
       #      return index
        #Binary Search 0(log n)
        # create start and end of array
        start, end = 0, len(nums) - 1
        #check if start is less than end
        while start <= end:
            # if it is, create the middle of the array
            middle = (start + end) //2
            #if target is equal to middle index
            if target == nums[middle]:
                #return middle index
                return middle
            # if target is less thatn middle index
            elif target > nums[middle]:
                #increment start with middle + 1
                start = middle + 1
                # if target is less that middle index
            elif target < nums[middle]:
                #decrement end with middle -1
                end = middle -1 
        return start