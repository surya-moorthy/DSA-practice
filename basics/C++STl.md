# C++ STL 

## Algorithms

## Container
   - Pair
   - Vector
   - List
   - Deque
   - Stack
   - PriorityQueue
   - Set 
   - MultiSet
   - UnorderedSet --> the time complexity will be O(1) but it will moves on to O(n) as the worst case.
   - Map --> Stores as Key , value Pair , the key and value may be any type , but keys are unique and sorted. 

## Functions

  Small piece of code that has prebuilt feature of what we need.

## Iterators
 --> Points the memory address of where the element is stored;

 **syntax:**
 ```
    datatype::iterators it = value;
 ```
 **Access**:
    
    *(it)

### Note :
   - Use emplace() when you're constructing a new object in-place — it's more efficient.
 
   - Use insert() when you're inserting an already-created object or want to be more explicit.

