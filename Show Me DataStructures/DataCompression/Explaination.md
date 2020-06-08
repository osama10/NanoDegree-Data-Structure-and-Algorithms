# Data Compression 

## Asumptions
- I am assuming that data will not be all spaces, empty strings or None. In case of any of these function will return `None`

## Explaination

I have followed the procedure defined in the question and did as it is described. I use heaps for priority queue as insertion and extractions are O(log(n)). I have used python's built `heapq` library for manking min heaps. Other than that I have made `DataCompressor` class that is responsible for encoding and decoding of data into huffman encoding. Other than that, each char in data is a Node having char and it's frequency. The over all data is stored in the form of Tree. For that I have use the same class from lectures of Tree

## Complexity

- ### Decoding

Decoding is pretty straighforward. I traverse the whole string of `encoded_data` take each bit and move left or right if bit is `'0'` or `1` respectively. If I got the leaf, I append it's char to the `decoded_string`. Since traversing tree is constant time here and I have to traverse the whole decoded_data, so it's complexity will be `O(n)` .

For space complexity, the resullt needs n space which is equal to number of character in decoded string so the space complexity will be **O(n)**

- ### Encoding

Encoding is divided in 4 parts . I will first analyze the complexity of each step and then the final complexity.

1) I am making frequency table. I am sending the processed string in it that just append `-` for spaces. This opearation is linear. Inside the method. I am traversing through the string provided and calculating the frequency. Since i am using dictionary for look up so the overall complexity of this step is `O(n)` where n is total number of char in the data .

2) Then I make a priority queue using heap. This step involves traversing through the all the pairs in frequency table and insert them in the queue. Traversing whole dictionary is linear time opearation and insertion in the heap in `O(log(m))` so the over all complexity will be `O(mlog(m))` where m is the total key, value pairs

3) The thirds step is creating huffman tree. This process will run until we create the whole tree . So it will be linear time `O(k)` where k is the total nodes in the tree

4) Last step involves encoding of data. This step involves two main operations. Make a bin_representation_table for char and then encode the data using that table. Both operatons are linear time so it's complexity will O(P)

since none of the above operation is nested, so the biggest complexity is O(mlog(m)) .i.e **Step 2** hence encoding's over all complexity will be **O(mlog(m))** 

For space complexity, there are four things that occupy memory. 
- Frequency table will have complexity of O(n) where n is the number of key value pairs
- then priority queue that will have the the same complexity
- Huffman tree will have O(K) complexity where K is the number of nodes
- Decoded string will have O(m) complexity, where O(m) is the number of char in the string

since all other things will be flushed out of the memory accept the decoded string and tree the overall complexity will be **O(m)** where m is total number of chars
