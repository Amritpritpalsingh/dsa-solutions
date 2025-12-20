class Solution(object):
    def countPrimes(self, n):
        l = [1 for i in range(n+1)]
        for i in range(2,int(n**.5)+1):
            if(l[i]!=0):
                for j in range(i*i,len(l),i):
                    l[j]=0
        cnt = 0
        for i in range(2,n):
            if(l[i]==1):
                cnt+=1 
        return cnt

        