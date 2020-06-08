# Rearrange Array Digits

## Explaination

The idea is to place the highest and second highest number at max digit postion, then less then them at next position until you completely traverse the array. For this we need to the array sorted . I use merge sort for that and **use the same code from the lectures**.

## Complexity

Two main steps are to sort the array and then build the two numbers. Sorting take O(nlog(n)) time while building the two numbers is O(n) time complexity. So the worst time complexity will O(nlog(n)).

I have use an auxilary space in merging. That makes the space complexity to O(n)
