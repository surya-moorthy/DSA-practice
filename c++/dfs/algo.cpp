#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

vector<int> dfs(int node, vector<int> &vis,stack<int> &st,vector<int> adj[]) {
   vis[node]  = 1;
   for (auto it : adj[node]) {
        if(!vis[it]) {
            dfs(it,vis,st,adj);
        }
   }
   st.push(node);
}

vector<int> topoSort(int V , vector<int> adj[]) {
    vector<int> vis(V, 0);
    stack<int> st;
    for(int i=0;i<V;i++){
        if(!vis[i]){
            dfs(i,vis,st,adj);
        }
    }
    vector<int> ans;
    while(!st.empty()) {
        ans.push_back(st.top());
        st.pop();
    }
    return ans;
}
