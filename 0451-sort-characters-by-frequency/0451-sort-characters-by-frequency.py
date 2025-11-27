class Solution(object):
    def frequencySort(self, s):
        map = {}
        for c in s:
            if c in map :
                map[c]+=1
            else :
                map[c] = 1

        sorted_keys = [k*v for k, v in sorted(map.items(), key=lambda x: x[1], reverse=True)]
        return "".join(sorted_keys)
