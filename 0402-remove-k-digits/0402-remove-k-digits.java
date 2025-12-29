class Solution {
    public String removeKdigits(String nums, int k) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < nums.length(); i++) {
            char c = nums.charAt(i);

            while (k > 0 && !st.isEmpty() && st.peek() > c) {
                st.pop();
                k--;
            }
            st.push(c);
        }

        // If k still > 0, remove from the end
        while (k > 0 && !st.isEmpty()) {
            st.pop();
            k--;
        }

        // Build result
        StringBuilder ans = new StringBuilder();
        while (!st.isEmpty()) {
            ans.append(st.pop());
        }
        ans.reverse();

        // Remove leading zeros
        while (ans.length() > 1 && ans.charAt(0) == '0') {
            ans.deleteCharAt(0);
        }

        return ans.length() == 0 ? "0" : ans.toString();
    }
}
