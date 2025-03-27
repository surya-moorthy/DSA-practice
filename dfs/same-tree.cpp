#include "iostream";

using namespace std;

struct Treenode {
    int val;
    Treenode *left;
    Treenode *right;
};

bool sameTree(Treenode *p, Treenode *q) {
   if (p == NULL && q == NULL) {
      return true;
   }
   if (p == NULL || q == NULL) {
    return false;
   }
   if(p->val == q->val){
      return sameTree(p->left,q->left) && sameTree(p->right,q->right);
   }
   return false;
}
