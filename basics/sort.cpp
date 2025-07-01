#include <bits/stdc++.h>

using namespace std;

// quick sort : Time complexity : O(nlogn) Space Complexity : O(1) , here we are iterating through only with the partition index has high in the qs func , not the all the elements(n elements) that is why space comp. is : O(1)  

void qs(int arr[],int low , int high){
     if(low < high){
         int partitiionIndex = partition(arr,low,high);
         qs(arr,low,partitiionIndex - 1);
         qs(arr,partitiionIndex + 1,high);
     }
}

int partition(int arr[],int low,int high) {
    pivot = arr[low];
    int i = low;
    int j = high;
    
    while(low < high){
        while(arr[i] <= arr[pivot] && i <= high - 1){
            i++;
        }
        while(arr[j] > arr[pivot] && j>=low + 1 ){
            j++;
        }
        if(i<j) swap(arr[i],arr[j]);
    }
    return j;
}

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
