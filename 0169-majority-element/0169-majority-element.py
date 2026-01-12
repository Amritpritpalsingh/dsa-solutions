class Solution(object):
    def majorityElement(self, nums):
        maxi_cnt =1
        nums.sort()
        maj_el = nums[0]
        cnt = 1
        n = len(nums)
        i=1
        while(i<n):
            if(nums[i] != nums[i-1]):
                if(cnt>maxi_cnt):
                    maxi_cnt = cnt
                    maj_el = nums[i-1]
                cnt = 1
            cnt+=1
            i+=1
        if(cnt>maxi_cnt):
            return(nums[i-1])
        else:
            return(maj_el)