#include "iostream";

using namespace std;

struct Treenode {
    int val;
    Treenode *left;
    Treenode *right;
};

bool hasPathSum(Treenode* root,int targetSum) {
    if(!root) return false;
    if(root->left == NULL && root->right) { return targetSum - root->val == 0;};
    targetSum = targetSum - root->val;
    return hasPathSum(root->left,targetSum) || hasPathSum(root->right,targetSum);
    
}