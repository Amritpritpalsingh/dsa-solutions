class Solution(object):
    def numRescueBoats(self, people, limit):
        cnt = 0 
        right= len(people)-1
        left = 0
        people.sort()
        while(left<=right):
            remain = limit - people[right]
            cnt+=1
            right -= 1
            if(left<=right and remain>=people[left]):
                left+=1
        return cnt
