class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        map = {}
        start_idx = -1
        cnt = 0
        len_s = len(s)
        len_t = len(t)
        l_ptr = 0
        min_len = float("inf")
        for i in range(len_t):
            if t[i] not in map:
                map[t[i]] = 1
            else:
                map[t[i]]+= 1 

        for r_ptr in range(len_s):
            if(s[r_ptr] in map):
                if(map[s[r_ptr]]>0):
                    cnt+=1
                map[s[r_ptr]]-=1
            while(cnt==len_t):
                if(s[l_ptr] in map):
                    map[s[l_ptr]]+=1
                    if(map[s[l_ptr]]>0):
                        cnt-=1
                if min_len > r_ptr - l_ptr + 1 :
                    min_len = r_ptr - l_ptr  + 1
                    start_idx = l_ptr
                l_ptr+=1

        return "" if start_idx == -1 else s[start_idx:start_idx + min_len]

        


            
