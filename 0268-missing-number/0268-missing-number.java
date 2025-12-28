class Solution {
    public int missingNumber(int[] arr) {
        
        int allSum = 0;
        int n = arr.length;
        int sum = ((n+1)*n)/2;
        for(int i = 0;i<n;i++){
            allSum+=arr[i];
        }
        return sum-allSum;
    }
}