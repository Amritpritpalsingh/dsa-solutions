import java.util.*;
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> st = new Stack<Integer>();
        int[] nge = new int[nums.length];
        int n = nums.length;
        for(int i = (n*2)-1 ; i >=0 ; i--){
            while(!st.empty() && st.peek()<=nums[i%n])st.pop();
            if(i<=n){
                if(st.empty()){
                    nge[i%n] = -1;
                }else nge[i%n] = st.peek();
            }
            st.push(nums[i%n]);
        }
        return nge;
    }
}