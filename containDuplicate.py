# Time:  O(n)
# Space: O(n)
#
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.
#只要有一个重复元素就返回true

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
    #利用set集合的特性，删除重复元素

if __name__ == '__main__':
    nums = [0, 2, 2, 0, 11, 15]
    print (Solution().containsDuplicate(nums))

