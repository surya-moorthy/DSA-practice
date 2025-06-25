#include <bits/stdc++.h>

using namespace std;

void PriorityQueue() {
    // largest value at the top
    // Max heap as default
        priority_queue<int, vector<int>> pq;
        pq.push(4);
        pq.push(2);
        pq.push(10);

        cout << pq.top() << endl;// largest elements gets print;
        pq.pop();

        //Minimum Heap
        priority_queue<int, vector<int>,greater<int>> Minpq;
        Minpq.push(5);
        Minpq.push(2);
        Minpq.push(8);
        Minpq.emplace(10);

        cout << Minpq.top() << endl;

        // push and pop --> O(logn)
        // top --> O(1)

}

int main() {
    
    PriorityQueue();
    return 0;
}

// Containers

// void Pair() {
//     pair<int ,pair<int , int>> p = {1,3, {3,4}};

//     cout << p.first << "  "<< p.second;
   
// }

void Vector() {
 vector<int> v = {1,3};
    vector<int>::iterator it = v.begin();
    
    for(int i : v) {
      cout << i << endl;
    }

    cout << *(it) << " ";

    for(vector<int>::iterator it = v.begin(); it != v.end() ; it++) {
        cout << *(it) << " ";
    }

    // auto assignation
    for( auto it = v.begin(); it != v.end(); it++) {
         cout << *(it) << " ";
    }

    // for each loop
    for(auto it : v) {
        cout << it << " ";
    }

    // vector erase

    // {10, 20, 12, 23}
    v.erase(v.begin() + 1);  //{20}

    // {10, 20, 12, 23,35}  
    v.erase(v.begin() + 2,v.begin() + 4);    // remain : {10,20,35}    //[start,end)

}

void List() {
    list<int> ls;
    ls.push_back(2); //{2}
    ls.emplace_back(4);  // {2,4}

    ls.push_front(5);  // {5,2,4}

    ls.emplace_front(); //{2,4}

    // rest functions same as vector 
    // begin, end, rebegin, rend, clear, insert, size, swap
}

void explainDeque() {
    deque<int> dq;
    dq.push_back(2); //{2}
    dq.emplace_back(4);  // {2,4}
    dq.push_front(5);  // {5,2,4}
    dq.emplace_front(3); //{2,4}

    dq.pop_back();
    dq.pop_front();

    cout << dq.back();

    cout << dq.front();

    // rest functions same as vector 
    // begin, end, rebegin, rend, clear, insert, size, swap    
}

void Stack() {
    // LIFO
    
    stack<int> st;
    st.push(1);
    st.push(2);
    st.pop();
    st.emplace(5);

    cout << st.top(); // prints what is at the top.
}

void Queue() {
    queue<int> q;
    q.push(1);
    q.push(2);
    q.emplace(4);

    q.back() += 5;

    q.pop();
}


void Set() {

    // sorted and unique
    
    set<int> st;
    st.insert(1);
    st.emplace(2);

}
