class Solution(object):
    def check(self, nums):
        dummy = nums[:]
        dummy.sort()
        length = len(nums)
        for i in range(length):
            flag = True
            first = dummy[0]
            for j in range(length - 1):
                dummy[j] = dummy[j+1]
            dummy[-1] = first
            for k in range(length):
                if(nums[k]!=dummy[k]):
                    flag = False
                    break
            if(flag is True):
                return True
        return False
        
        