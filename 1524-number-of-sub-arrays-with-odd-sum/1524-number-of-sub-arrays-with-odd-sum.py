class Solution(object):
    def numOfSubarrays(self, arr):
        cnt_even = 1
        cnt_odd = 0
        pre_sum = 0 
        res = 0
        MOD = 10**9 + 7
        n = len(arr)
        for i in range(n):
            pre_sum+=arr[i]
            if(pre_sum%2==0):
                res+=cnt_odd
                cnt_even+=1
            else:
                res+=cnt_even
                cnt_odd+=1
            res%=MOD
        return res
