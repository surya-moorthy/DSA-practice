#include <iostream> 

using namespace std;

// functions 
// void -> function that does not return anything! 
// return -> 

void printName(int &num) {
    num = num + 5;
    cout << num << endl;
    num = num + 5;
}

int main() {
    int num = 20;
    printName(num);
    cout << num << endl;
    return 0;
}



























// int main() {
//     // int age;
//     int i; 

//     // cin >> age;
//     // if(age <= 18 ){
//     //     cout << "You are a child!";
//     // }

//     // int marks;
//     // cin >> marks;

//    // actual if else 

//     // if(marks < 25) {
//     //     cout << "F"
//     // } else if(marks >= 25 && marks <= 44){
//     //     cout << "E";
//     // } else if(marks >= 45 && marks <= 69){
//     //     cout << "D";
//     // } else if(marks >= 70 && marks <= 89){
//     //     cout << "C";
//     // } else if(marks >= 90 && marks <= 100){
//     //     cout << "B";
//     // } else if(marks >= 25 && marks <= 44){
//     //     cout << "A";
//     // } 


//     // optimized 
    
//     // if(marks < 25) {
//     //     cout << "F";
//     // } else if( marks <= 44){
//     //     cout << "E";
//     // } else if( marks <= 69){
//     //     cout << "D";
//     // } else if( marks <= 89){
//     //     cout << "C";
//     // } else if(marks <= 100){
//     //     cout << "B";
//     // } else if(marks <= 44){
//     //     cout << "A";
//     // } 

//     // if(age < 18) {
//     //     cout << "You are not eligible for the job!";
//     // } else if(age <= 57) {
//     //     cout << "You are eligible for the job";

//     //     if(age >= 55 ) {
//     //         cout << "retirement is soon.";
//     //     }
    
//     // } else {
//     //     cout << "you are retired.";
//     // }
//     // int day;
//     // cin >> day;

//     // switch (day)
//     // {
//     // case 1:
//     //     cout << "Monday";
//     //     break;
//     // case 2:
//     //     cout << "Tuesday";
//     //     break;
//     // case 3:
//     //     cout << "Webnesday";
//     //     break;
//     // case 4:
//     //     cout << "Thursday";
//     //     break;
//     // case 5:
//     //     cout << "Friday";
//     //     break;
//     // case 6:
//     //     cout << "Saturday";
//     //     break; 
//     // case 7:
//     //     cout << "Sunday";
//     //     break;
    
//     // default:
//     //     cout << "Invalid day";
//     //     break;
//     // }

//     // return 0;

//     // int a[4];
     
//     // // collection of similar data type
//     // a = [1,2,3,4];

//     // cout << a;
//     // for( i= 1;i < 100; i = i + 1){
//     //     cout << "HI" << i << endl;
//     // }
//     //  while(i%2 == 0) {
//     //         cout << "even" << endl;
//     //     }
   
//     // return 0;


// }