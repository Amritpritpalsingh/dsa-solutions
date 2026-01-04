class Solution(object):
    def totalFruit(self, f):
        map = {}
        ans = 0
        l = 0
        for i in range(len(f)):
            if(len(map)>2):
                map[f[l]]-=1
                if(map[f[l]]==0):
                    del map[f[l]]
                l+=1
           
            if(f[i] in map):
                map[f[i]]+=1
            else:
                map[f[i]]=1
               

            if(len(map)<=2):
                ans = max(ans,i-l+1)


        return ans
