#include <bits/stdc++.h>

using namespace std;

void frequency(int arr[] ,int n) {

    // for(int i=0;i<n;i++) {
    //     int q;
    //     cin >> q;

    //     arr[q] += 1;
    // }

    // int q;
    // cout << "enter the  no of elements you want to query";
    // cin >> q;
    // while(q--) {
    //     int number;
    //     cin >> number;

    //     cout << " the number " << number << "appeared is " << arr[number] << endl; 
    // }

    // return 0;
    unordered_map<int , int> mpp;
    
    for(int i=0;i<n;i++) {
        mpp[arr[i]]++;
    }

    for(auto it : mpp) {
        cout << it.first << " " << it.second << endl;
    }  
}

int main() {
    int arr[] = {10,5,10,15,10,5};
    int n = sizeof(arr) / sizeof(arr[0]);
    frequency(arr,n);
    return 0;

}


