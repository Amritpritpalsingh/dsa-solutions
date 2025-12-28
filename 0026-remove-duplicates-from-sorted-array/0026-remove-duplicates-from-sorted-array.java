class Solution {
    public int removeDuplicates(int[] nums) {
        int  i = 0;
        int  j = 1;
        int n = nums.length;
        while (j<n){
            if(nums[i]!=nums[j]){
                i+=1;
                nums[i] = nums[j];
            }
            j+=1;
        }
        return i+1;
    }
}