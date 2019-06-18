# Problem 1. Square Root of an integer

Since the expected time complexity to solve this problem was O(log n) I have decided to use the binary search algorithm
 between 0 and the number given to find the floored square root number.

Binary search guarantees a complexity of O(log n) since we are halving the array in halves every time we iterate.

Space complexity is O(1) since we are using the same amount of variables to calculate the square root of any number.