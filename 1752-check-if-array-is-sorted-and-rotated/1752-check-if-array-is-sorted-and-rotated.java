class Solution {
    public boolean check(int[] nums) {
        int n = nums.length;
        if(n==1) return true;
        int cnt = 1;
       
        for(int i = 1 ; i<n*2;i++){
            if(nums[i%n]>=nums[(i-1)%n]){
                cnt+=1;
            }else{
                cnt=1;
            }
            if(cnt==nums.length) return true;
            
        }
       
        return false;

    }
}