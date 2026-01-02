#include<bits/stdc++.h>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> map;
        int left = 0, cnt = 0;
        for(int right = 0; right < s.length(); right++) {
            map[s[right]]++;
            while(map[s[right]] > 1) {
                map[s[left]]--;
                left++;
            }
            cnt = max(cnt, right - left + 1);
        }
        return cnt;
    }

};