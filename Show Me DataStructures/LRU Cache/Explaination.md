# LRU Cache Explaination

### Exalpaination

I have implemented the LRU cache using two data structures. One is the dictionary ( hash map ) and a queueuq using doubly link list. Reasons of using this approach is define below.

- The main idea behind the usage of dictionary is the O(1) lookup in case of cache hit . 
- I use queue to maintain the track of usage of cached data. So according to the policy, it should remove the Least recently used node from it. I use this track by always keep the LRU data at the top of the queue for. and from it if cache capacity is full. When a new items is added , it will always be added to the tail. If capacity is ful, queue will be dequeue the top element. In case of a hit , i use `make_tail` method that removes that node from it's current position and makes it tail 
- Reason of using Double link list is that the insertion and deletion from Link list O(1) if nodes is give, Since i need to reference the prev node to avoid the traversal during insertion that's why I used Doubly link lst.

### Complexity

Hash map has O(1) lookup time. Since all the operations in the queue are also O(1) the over all complexity will be of O(1) 

Space complexity will also be O(1) as no extra space is required for set and get operations
