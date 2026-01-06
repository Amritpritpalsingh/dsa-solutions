class Solution(object):
    def countVowelSubstrings(self, word):
        cnt = 0
        s = "aeiou"
        for i in range(len(word)):
            if(word[i] in s):
                map = {}
                for j in range(i,len(word)):
                    if(word[j] in s):
                        if(word[j] in map):
                            map[word[j]]+=1
                        else:
                            map[word[j]]=1
                        
                        if(len(map)==5):
                            cnt+=1
                    
        return cnt
                    



            
        