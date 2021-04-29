"""
26. Remove Duplicates from Sorted Array
Easy

3817

6910

Add to List

Share
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # # this problem can be used with a solution technic called two pointers                that is i and j 0(n)
        # i = 0 #slow pointer
        # j = 0 #faster pointer
        # # we will loop array nums
        # for j in range(len(nums)):
        #     #if j is not equal to i
        #     if nums[j] != nums[i]:
        #     # increment i
        #         i += 1
        #     # and assign i to j
        #         nums[i] = nums[j]
        #     # if its equal we do nothin, we just increment i
        # return i + 1
        # better solution binary search 0(log n)
        # declare i to beginning of array, and l to end of the array
        i = 0
        l = len(nums) - 1
        # check that i is minus than l 
        while i < l:
            # if array i is equal to array i + 1, 
            if nums[i] == nums[i + 1]:
                # delete array i + 1
                del nums[i + 1]
                # and after reset i one less to the left
                l -= 1
                # or else increment i + 1 to the right
            else:
                i += 1