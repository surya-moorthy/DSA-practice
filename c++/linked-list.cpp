#include <iostream>

using namespace std;

//structure of a node in a linked list

struct Node {
    int data;
    Node* next;

    //when creating a new node 
    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class Linkedlist {
    Node* head = nullptr;
    public: 
       void newNode(int data) {
        Node* temp = new Node(data); 
        if(head == nullptr) {
            head = temp;
        }
       }
       void insertAtBeg(int data) {
         Node* temp = new Node(data);
         temp->next = head;
         head = temp;
       };
       void display() {
          Node* temp  = head;
          while(temp != nullptr){
            cout << temp->data << " ";
            temp = temp->next;
          }
       }
       void insertAtEnd(int data) {
          Node* newNode = new Node(data);
          Node* temp  = head;
          while(temp->next != nullptr){
            temp = temp->next;
          }
          temp->next = newNode;
       }
       void insertAtMiddle(int data , int pos) {
          Node* newNode = new Node(data);
          Node* temp = head;    
          for(int i=1;i<pos-1;i++){
             temp = temp->next;
          }
          newNode->next = temp->next;
          temp->next = newNode;
       }
      void delAtMiddle(int pos) {
        Node* temp = head;    
        for(int i=1;i<pos-1;i++){
           temp = temp->next;
        }
        Node* delNode = temp->next;
        temp->next = delNode->next;
     }

     void reverseTheList() {
        Node* current;
        Node* next;
        Node* prev;
        current = head;
        prev = NULL;
        
        while(current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
     }

};
  
int main() {
    Linkedlist list;
    list.newNode(1);
    list.insertAtEnd(2);
    list.insertAtEnd(4);
    list.insertAtEnd(5);
    list.insertAtEnd(6);
    list.insertAtMiddle(3,3);
    list.delAtMiddle(2);
    cout << "LinkedList :" << " ";
    list.display();
    cout << "ReverseList :" << " ";
    list.reverseTheList();
    list.display();
}
