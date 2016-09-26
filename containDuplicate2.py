# Time:  O(n)
# Space: O(n)
#
# Given an array of integers and an integer k, return true if 
# and only if there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i,num in enumerate(nums):
            if num not in dic:
                dic[num] = i
            else:
                if i - dic[num] <= k:
                    return True
                else:
                    dic[num] = i
                    #更新位置（之前的太远）
        return False
if __name__ == "__main__":
    print (Solution().containsNearbyDuplicate([1,2,3,4,5,1],3))

