class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        st = []
        nge = []
        j = 0
        maps={}
        for i in range(len(nums2)-1,-1,-1):
            
            while(len(st)!=0 and st[-1]<nums2[i]):
                st.pop()
            if(len(st)==0):
                maps[nums2[i]]=-1

            else:
                maps[nums2[i]]=st[-1]
            st.append(nums2[i])
        
        for i in range(len(nums1)):
            nge.append(maps[nums1[i]])
        return nge





        