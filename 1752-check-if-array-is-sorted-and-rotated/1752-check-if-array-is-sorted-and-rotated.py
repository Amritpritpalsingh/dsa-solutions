class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 1
        n = len(nums)
        if(n==1):return True
        for i in range(1,2*n):
            if(nums[(i-1)%n]<=nums[i%n]):
                cnt+=1
            else:
                cnt=1
            if(cnt==n):
                return True
        return False
            
       
    
        