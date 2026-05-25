#include "bits/stdc++.h"

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<vector<int>> intervals = {{1,2},{3,4},{1,3},{2,3}};
    
    sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) {
        return a[1] < b[1];
    });

    for(int i = 0; i < intervals.size(); i++) {
        for(int num : intervals[i]) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}