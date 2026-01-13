class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l_ptr = 0
        r_ptr = 0
        temp = [-1] * (m+n)
        curr = 0
        while l_ptr < m and r_ptr < n :
            if nums1[l_ptr] <= nums2[r_ptr]:
                temp[curr] = nums1[l_ptr]
                l_ptr+=1
            else:
                temp[curr] = nums2[r_ptr]
                r_ptr+=1
            curr+=1
        while l_ptr < m :
            temp[curr] = nums1[l_ptr]
            l_ptr+=1
            curr+=1

        while r_ptr < n :
            temp[curr] = nums2[r_ptr]
            r_ptr+=1
            curr+=1
        len_array = len(temp)
        for i in range(len_array):
            nums1[i] = temp[i]
        


