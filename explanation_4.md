# Problem 4. Dutch National Flag

To solve this problem I used three arrays to store the elements based on the number and then I concatenate according
to the numbers' order, i.e. first 0, then 1 and then 2

I loop just once the initial input_list array and based on the elements I add them to the particular array.

The runtime complexity is O(n) being n the length of the input list which we need to loop once.

The space complexity is also O(n) since the total size of the three new arrays is the length of the input list, n.