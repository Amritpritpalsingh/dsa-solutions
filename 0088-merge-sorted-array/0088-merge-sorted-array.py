class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k_ptr = len(nums1)-1
        l_ptr = m-1
        r_ptr = n-1
        while(r_ptr >=0):
            if(l_ptr>=0 and nums1[l_ptr]>=nums2[r_ptr]):
               
                nums1[k_ptr] = nums1[l_ptr]
                l_ptr-=1
            else:
                nums1[k_ptr] = nums2[r_ptr]
                r_ptr-=1
                

            k_ptr-=1
        


