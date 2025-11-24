/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<long long>p1;
    vector<long long>q1;
    void check1(TreeNode* p){
        if(p==NULL){p1.push_back(-111111); return;}
        check1(p->left);
        check1(p->right);
        p1.push_back(p->val);
        
    }
    void check2(TreeNode* q){
        if(q==NULL){q1.push_back(-111111); return;}
        check2(q->left);
        check2(q->right);
        q1.push_back(q->val);
        
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        check1(p);
        check2(q);
        if(p1==q1) return true;
        else return false;
    }
};