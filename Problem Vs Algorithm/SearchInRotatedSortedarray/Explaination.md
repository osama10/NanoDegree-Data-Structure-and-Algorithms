# Search in Rotated Sorted Array

## Explaination:
The idea is to find the smallest element and make it a `pivot`. Check if the number lies between it and the last element, if true then search this part of array else search from first element to element before the `pivot`

## Complexity

This problem divides in two parts. 1) finding the smallest element . 2) Finding the value . Both opearation uses binary search that makes the overall complexity to be O(log(n)). Since I am not using any extra space, then space complexity is O(1)