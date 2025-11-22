class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def isPos(p,s,mp):
            cnt = 1
            have = 0
            for i in range(0,len(p)):
                if(have+p[i]<=mp):
                    have += p[i]
                else:
                    have = p[i]
                    cnt+=1
            if(cnt>s):return False
            else :return True

        def find(p,s):
            low = max(p)
            high = sum(p)
            while(low<=high):
                mid = low + (high-low)//2
                isPoss = isPos(p,s,mid)
                if(isPoss):
                    high = mid - 1
                else :
                    low = mid +1
                    
            return low
            
        return find(nums,k)

