# Problem 4. Dutch National Flag

To solve this problem I initially used three arrays to store each of the different numbers but thanks to
the reviewer's suggestion I ended up using the same array to order the elements or what is called in-place
sorting.

I used two pointers, one to point where the index for 0s is and the other to point the index for 2s.
I loop just once the initial input_list array and based on type of number I swap the current element with 
 the right pointer, that is, index_0 if it is a 0 or index_2 if it is a two
 
The runtime complexity is O(n) being n the length of the input list which we need to loop once.

The space complexity is also O(1) that is, running this algorithm the size won't growth since it will only
use the initial array because the sorting is `in-place`