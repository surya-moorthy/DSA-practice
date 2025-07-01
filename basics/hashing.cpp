#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++) {
        cin >> arr[i];
    }
    //pre-compute
    unordered_map<int, int> mpp;
    for(int i=0;i<n;i++){
        mpp[arr[i]]++;
    }

    for(auto it:mpp) {
            cout << it.first << "->" << it.second << endl;

    }

    int q;
    cin >> q;
    // fetch
    while(q--) {
        int number;
        cin >> number;

        cout << mpp[number] << endl;
    }
    return 0;
}
//     int main() {
//         string s;
//         cin >> s;

//         //pre compute
//         int hash[26] = {0};
//         for(int i= 0; i < s.size(); i++){
//             hash[s[i] - 'a']++;
//         }

//         int n;
//         cin >> n;
//         while(n--) {
//             char cha;
//             cin >> cha;
//             // fetch 
//             cout << hash[cha - 'a'] << endl;
//         }
//         return 0;
//     }

//     /*
//     // hashing as prestoring and computation..
// void precomputaiton(int n , int arr[] ) {
//      int q;
//      cout << "Enter which integer you want to count:" << endl;
//      cin >> q;
//        cout << "Enter the elements:" << endl;
//      while(q--) {
//         int numbers;
//         cin >> numbers;
//         cout << arr[numbers];
//      }
// }

// int main() {
//     int n;
//     cout << "Enter number of elements to add:" << endl;
//     cin >> n;
//     cout << "Enter the elements to add:" << endl;
//     int arr[n] = {0};
//     for(int i=0;i<n;i++){
//         int q;
//         cin >> q;
//         arr[q] += 1;  
//     }
//     precomputaiton(n , arr);
//     return 0;
// }
// */