
# Block Chain

## Explaination
Implemented block chain using simple single link list. For hashing, I include data, timestamp and prev_hash to make it unique every time. I keep the head and tail of the Block Chain for fast append opearating

## Complexity

Considering cal_hash function constant time. The append function on Block chain will also be O(1) because i keep the track if tail and head so it save me traversing the whole Blockchain every time. The string representation of Blockchain needs to traverse the whole chain which makes it of O(N)

Since we are not using any extra space, the space complexity will be O(1)