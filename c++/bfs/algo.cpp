#include "iostream"
#include "vector"
#include "queue"

using namespace std;

vector<int> bfs(vector<vector<int>> &adj,int s) {
    int V = adj.size();
    queue<int> que;
    vector<bool> visited(V, false);

    visited[s] = true;
    que.push(s);
    vector<int> res;

    while(!que.empty()) {
       int curr = que.front();
       que.pop();
       res.push_back(curr);

       for(int x : adj[curr]) {
         if(!visited[x]){
             visited[x] = true;
             que.push(x);
        }
       }
    }
   return res;
}

int main() {
    vector<vector<int>> adj = { {2, 3, 1}, {0},
                                {0, 4}, {0}, {2}};

    int src = 2;
    vector<int> res = bfs(adj,src);
    for(int x: res) {
        cout << x << " "; 
    }
}