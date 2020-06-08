# Autocomplete with Tries

## Explaintion

I implemented the trie as it's defined in the course and this example. Since the problem is to finc the suffix. I made the autocomplete function that gets the suffix of the given prefix and then combine them with prefix to give the final recommendation. So suffix is not directly used in the examples but inside the autocomplete function of trie.

## Complexity 

- **Insert** funtion adds the word in the trie. Worst case will be when the characters in the word are all different from previous characters at each level. So this will make the time complexity to O(n) where n is the number of total character inside the word that is pass in insert function. Since no extra space is required, the space complexity will be O(1)

- **Find** find function traverse through the trie ad search for the word by checking all the matching keys if exist till the last char in the word that is need to be searched. Since searching in the dictionary is O(1), so it's time complexity will also be O(n) where n is the number of chars in the word. It also doesn't required any extra space so the space complexity will be O(1)

- **autocomplete**  This function get first finds the the node of the prefix that's passed , then it check traverser throug it's children and there children which is similar to depth first search. So the time complexity will be O(n) where n is the number of children, prefix has. 

Since it use recursion, stack needs to be maintained upto the last child, so space complexity will also be O(n)

