# File Recursion

## Explaination:
This file structure is sort of a tree struct where the top directory is a root node and has files and subdirectories as it's children. Since we have to find in every subdirectory for the file passed as suffix, I used DFS for it . It works like this, it take all the children starting from Root and in a list. Then traverse through the loop and check for the file, if it found one and it has right suffix, it adds in to the `resultant_urls` list else it recursively calls the same method for the direcotry paths for it's children. 

## Complexity
Since we have to traverse the complety directory tree, the complexity will O(n) where n is the total number of all the files and directories in the root url

In worst case the file wont be inside the directory and it will have search in all the sub-directories. Since it needs recursive call, the complexity will be the space needed for all recuresive calls . It will be O(n) where n is the sum of all the sub direcotries inside the parent direcotry