#include "bits/stdc++.h"

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int volumes[n];
    for(int i = 0; i < n; i++) {
        cin >> volumes[i];
    }

    int count = 0;

    int curr_volume = volumes[0];

    if(curr_volume %2 != 0) {
        if(curr_volume != 1) {
             count++;
            curr_volume /= 2;
        }

    }

    for(int i = 1; i < n; i++) {
        while(volumes[i] < curr_volume) {
                count++;
                volumes[i] *= 2;
        }
        while(volumes[i] > curr_volume) {
                count++;
                volumes[i] /= 2;
        }

        curr_volume = volumes[i];
    }

    cout << count << "\n";
}