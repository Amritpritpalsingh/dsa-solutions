class Solution(object):
    def removeDuplicates(self, nums):
        set_nums = set()
        
        for i in range(len(nums)):
            set_nums.add(nums[i])
        k = len(set_nums)

        for i in range(len(set_nums)):
            nums[i] = set_nums.pop()

        return k