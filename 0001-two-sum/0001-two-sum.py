class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l =[]
        d = {}
        i=0
        for idx, num in enumerate(nums):
            if target - num in d:
                l.append(d[target - num])
                l.append(idx)
                break
            d[num] = idx
        return l
    
        