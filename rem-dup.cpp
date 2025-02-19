#include  <iostream>
#include <vector>

using namespace std;

int main () {
    int n;
    cout << "Enter the range of array:";
    cin >> n;
    std::vector<int> nums(n);
    std::vector<int> temp_nums(n);
    cout << "Enter the elements you want to add:";
    for (int i=0 ; i < n; i++){
        cin >> nums[i];
    }
    cout << "The array you have given:";
    for (int num : nums){
       cout << num << " ";
    }
    int left = 0;
    int right = nums.size();
    int temp=nums[left];
    while (left < right)  {
        if (nums[left + 1] == temp) {
            temp_nums = nums[:left+1] + nums[left+2:] + _;
            nums = temp;
            left++ ;
        }
    }
    cout << "The array you have given without duplicate:";
    for (int num : nums){
       cout << num << " ";
    }
    return 0;
}

