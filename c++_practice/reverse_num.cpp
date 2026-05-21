#include "bits/stdc++.h"

using namespace std;

int main() {
    ios::sync_with_stdio(false);

    int n;

    cout << "Enter the num : ";
    cin >> n;

    int result = 0;
    
    while(n > 0) {
        result = result * 10 + n % 10;
        n /= 10;
    }

    cout << "Resultant reverse : " << result << "\n";
    
    return 0;
}