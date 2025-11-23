class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = len(needle)
        while(i<=len(haystack)-len(needle)):
            if(haystack[i:j+i]==needle):
                return i
                break
            else:
                i=i+1
        else:
            return -1

        