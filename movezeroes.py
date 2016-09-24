# Time:  O(n)
# Space: O(1)

''' Given an array nums, write a function to move all 0's
 to the end of it while maintaining the relative order 
 of the non-zero elements.
 
 For example, given nums = [0, 1, 0, 3, 12], after
calling your function, nums should be [1, 3, 12, 0, 0].
 Note: You must do this in-place without making a copy of the array.
 Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[position] = nums[position], nums[i]
                position +=1
                

class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[position] = nums[i]
                position +=1
        for i in range(position,len(nums)):
            nums[i] = 0
            
if __name__ == '__main__':
    nums = [0, 2, 7, 0, 11, 15]
    Solution().moveZeroes(nums)
    print nums
