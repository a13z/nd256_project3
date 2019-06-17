# Problem 3. Rearrange Array Elements

To solve this problem and based on some comments in the student hub from students and mentors, I used the counting sort
 algorithm to sort the array. This algorithm has a runtime complexity of O(n + k) being n the number of elements in 
 the array and k being the range in which the elements of the array are. According to the description of the problem
  the range is [0,9] therefore k is 9. 

I created a function which implements the counting sort and it is called in the rearrange_digits function.

Once the input_list is sorted using the counting sort, I loop it in descending order and I separate the values 
in two arrays, each getting a value from the top.
Then I convert the array to a number taking its index positions as a power of 10.

The worst case Big O is O(n)

The space complexity is also O(n)


 
 