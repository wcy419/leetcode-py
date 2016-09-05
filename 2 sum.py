class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []


if __name__ == '__main__':
    print ("index1=%d, index2=%d" % Solution().twoSum((2, 7, 11, 15), 9))
