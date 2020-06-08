# Active Directory

## Explaination
I model this problem as tree where a group can have sub groups and user as children. The search of user involves two parts
- Search for the user in the group's immediate user
- Search the users in the group's sub-group

Since it involves searching user array, i make a set and always append user-id when appending a user to a group. This gives me effiecient look up when i am searching for user. 

## Complexity

Since theres no concrete order of this tree, search involes traversing through whole tree for finding the user. I use depth-first search for that which has O(N). Searching user will be in constant time because of sets so the over all complexity will be O(N) where N will the sum of all sub groups inside the group

In case of sub groups and Id that doesnt exist, it will check through all subgroups recursively that needs stack for the recursive calls. So it will have **O(n)** of space complexity where n is total number of sub groups
