# Union and Intersection 

## Asumption
- I am assuming that answer will only have the unique elements or will not have duplicates

## Explaination
The solution is simple. I traverse both link list one by one and put them in there respective sets. This will take O(N) time. Then I take the union and intersection of the two sets. This is also and O(n) time operation. Then i construct the the new link list from the result of union and intersection . This is also in O(n) time

## Complexity
Since all the operations done are in O(n) time. The overall complexity will be O(n)

There will be new list that's made for intersection and Union . They both have the the complexity of **O(n)** where n is the number of elements in the resultant linklist of after union and intersection 