class Solution(object):
    def findRestaurant(self, l1, l2):
        len1  = len(l1)
        len2 = len(l2)
        map = {}
        array = []
        n = float("inf")
        for i in range(len1):
            map[l1[i]] = i
      
        for j in range(len2):
            if(l2[j] in map):
                if(n>(map[l2[j]] + j)):
                    array=[]
                    array.append(l2[j])
                    n = (map[l2[j]] + j)
                elif(n==(map[l2[j]] + j)):
                    array.append(l2[j])
                    
        return array

            



                

        