class Solution(object):
    def majorityElement(self, nums):
        cnt = 0
        n = len(nums)
        maxi = nums[0]
        for i in nums:
            if(cnt==0):
                maxi = i
                cnt = 1
            elif i==maxi:
                cnt+=1
            else:
                cnt-=1
        cntMax = 0
        for i in nums:
            if(i==maxi):
                cntMax+=1
        if(cntMax>(n//2)):
            return maxi
        else:
            return -1
        