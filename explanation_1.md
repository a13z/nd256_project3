# Problem 1. Square Root of an integer

Since the expected time complexity to solve this problem was O(log n) I have decided to create an array of numbers from 
0 to the number given divided by 2 (since the root square is smaller than the half of the number) and then to use binary
 search to find the floored square root.

Binary search guarantees a complexity of O(log n) since we are halving the array in halves every time we iterate.

Space complexity is O(n/2) the way I implemented given that the square root of a number is small compared to the number
  i.e. at least smaller than the half of the number. Because of this, I defaulted the square root of 0 and 1.