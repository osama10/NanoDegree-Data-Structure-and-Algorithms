# Http router using tries

## Explaination

Follows what is the defined in the problem statement. In TrieRotuerNode, I made handler instead of is word.  I have take an assumption that a path must start from `'/'` else it will not be a valid path.

## Complexity

Since every operation is routed to Trie, so the complexity of `add_handler` and `look_up` of Router is depends on `insert` and `find` method. 

- **add_handler** it uses insert method in `Trie` to add the path and handler. The insert method adds the the words in the path inside trie. The. worst time complexity will O9(n) which is the number paths in a a given path . `split_path`  method uses a paths arr which is the paths that we get after splitting the path. So the space. complexity wil O(n) where n is number of paths after spliting

- **look_up** it uses insert method to find the path. So the time complexity depends on the path that we are looking on. So the complexity will be O(n) where n is the number of paths that are in the path that we need to search. `split_path`  method uses a paths arr which is the paths that we get after splitting the path. So the space. complexity wil O(n) where n is number of paths after spliting

- **Find** find function traverse through the trie and search for the path by checking all the matching keys if exist till the last path in the word that is need to be searched. Since time complexity of checking a Key in dictionary is O(1), it's time complexity will be O(n) where n is the number of paths in the in a single path. It also doesn't required any extra space so the space complexity will be O(1)