#include <bits/stdc++.h>
using namespace std;

// time complexity : O(nlogn) space complexity : O(n)

void mergeSort(int arr[],int low , high){
    if low >=-high return;
    int mid = (low + high)/2; 
    mergeSort(arr,low,mid);
    mergeSort(arr,mid + 1,high);
    Merge(arr,low,high,mid);
}

void Merge(int arr[],int low,int high,int mid){
    vector<int> temp;
    int left = low;
    int right = mid + 1;
    while(left <= mid && right && high){
        if(arr[left] >= arr[right]){
            temp.push_back(arr[right]);
            right++;
        }
        else{
             temp.push_back(arr[left]);
            left++;
        }
    }

    while(left <= mid){
        temp.push_back(arr[left]);
            left++;
    }

    while(right <= high){
         temp.push_back(arr[right]);
        right++;
    }

    for(int i=low;i<=high;i++){
        arr[i] = temp[i - low];
    }
}


int main(){
    return 0;
}

