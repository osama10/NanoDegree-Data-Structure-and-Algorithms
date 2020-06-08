# Unsorted Integer Array

## Explaination

I use simple algorithm. Initialize two variables, max and min and set them with min possible and max possible respectively. Then I traverse the whole array and check if the num is greater then the max set max with this number . If number is smaller then the min, then set this num to min. return max and min

## Complexity

It requires single traversal of array which is O(n) time complexity.
Since it's doesn't require any additional space except the resultant variable, the space complexity us O(1) 