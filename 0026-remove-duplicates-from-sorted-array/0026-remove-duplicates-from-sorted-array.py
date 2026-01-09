class Solution(object):
    def removeDuplicates(self, nums):
        unique = sorted(set(nums))
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)