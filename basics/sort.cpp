#include <bits/stdc++.h>

using namespace std;

// selection sort

// time complexity : n(n+1)/2 = O(n*2)

void swap(int i,int j){
    int temp = i;
    i = j;
    j = temp;
}

void selection_sort(int arr[],int n){
     for(int i=0;i<=n-2;i++){
        int min = i;
        for(int j=i;j<=n-1;i++){
           if(arr[j] < arr[min]) {
            min =j;
           }
           swap(arr[i],arr[min]);
        }
     }
}

void bubble_sort(int arr[],int n){
    // optimization 
    int didSwap = 0;
    for(int i=n-1;i>=0;i++){
        for(int j=0;j<=i-1;j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j],arr[j+1]);
                 didSwap = 1;
            }
           
        }
        if(didSwap == 0){
            break;
        }
    }
}

void insertion_sort(int arr[],int n){
    for(int i=0;i<=n-1;i++){
        j=i;
        while(j > 0 && a[j-1] > a[j]){
            swap(arr[j],arr[j-1]);
            j--;
        }
    }
}


void merge(int arr[],int low, int high,int mid){
    
}


int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    selection_sort(arr,n);
     for(int i=0;i<n;i++){
        cout << arr[i];
    }
    return 0;
}