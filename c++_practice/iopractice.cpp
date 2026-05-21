#include "bits/stdc++.h"

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // sum of n numbers and even number and odd numbers

    int n;

    cin >> n;


    int arr[n];

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int sum = 0;
    int odd = 0;
    int even = 0;

    for(int i = 0; i < n; i++){
        sum += arr[i];

        if ((arr[i] % 2) == 0) {even += arr[i];}
        else {odd += arr[i];}
    }

    cout << "sum : " << sum << "\n";
    cout << "even sum : " << even << "\n";
    cout << "odd sum : " << odd << "\n";

    return 0;
}