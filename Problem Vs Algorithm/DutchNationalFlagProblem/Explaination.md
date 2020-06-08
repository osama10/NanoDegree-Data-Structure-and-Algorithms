# Dutch National Problem

## Explaination

The idea is to place '0' and '2' at there proper place and this will result in the placement of '1' at it's right place. Algo works this way.

- There will be three pointers zero_index, current_index, second_index . 
- zero and current wil be initilazed from 0 while second index will be len(arr) - 1
- run loop until current <= second_index
- check value at current index 
	- if it's '0'
		- swap values at current and zero index
		- increnment both index by 1
	-  if it's '2'
		- swap values at current and second index
		- decrement second index
	- else
		- it will be one let's keep it as it is and increment current

- return arr

## Complexity

Since this require on pass through array , runtime complexity will be O(n) where n is total elements in array.
Since it doesnt use any extra space the space complexity will be O(1) 

