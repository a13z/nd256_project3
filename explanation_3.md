# Problem 3. Rearrange Array Elements

To solve this problem and based on some comments in the student hub from students and mentors, I used the counting sort
 algorithm to sort the array. This algorithm has a runtime complexity of O(n + k) being n the number of elements in 
 the array and k being the range in which the elements of the array are. According to the description of the problem
  the range is [0,9] therefore k is 9. 

I created a function which implements the counting sort and it is called in the rearrange_digits function.

Once the input_list is sorted using the counting sort, I loop it in descending order and I separate the values 
in two arrays, each getting a value from the top.
Then I convert the array to a number taking its index positions as a power of 10.

The worst case Big O for this problem is approximated to O(n). Let's analyse why.

The rearrange_digits function has one call to counting_sort function and three loops.

The counting_sort function has three arrays if we count the initialisation of the count array to 0s.

`    count = [0 for _ in range(k+1)] # This has a O(m) being m (k + 1) the number of different numbers in the array in our case is k + 1

    # iterate through the array and count the number of times a number appears in the array
    # and stores them in the count array
    # this is O(n) being n the number of elements in the array
    for number in array:
        count[number] += 1 

    # iterate through count array and add a number as many times as appeared in the original array
    # but in ascending order
    # this is O(m) being m (k + 1) the number of different items appearing in the array
    for number, times in enumerate(count):
        output += [number] * times
`

Therefore, the counting_sort function has O(m) + O(n) + O(m) which is
O(2m + n)
For our particular problem, we know that m is between 0 and 9 (included) so we have 10 different numbers
in all cases and just depends on the number of the array to sort. So the complexity is:
O(10 + n) or O(n + 10). We can approximate this to O(n) for the counting sort function.

After we have called the counting_sort function, we have three loops:
`   
    
    # the complexity is O(n) being n the number of elements of the array
    for index in range(sorted_array_size, -1, -1): 
        new_index = sorted_array_size - index
        if new_index % 2:
            number1_array.append(sorted_array[new_index])
        else:
            number2_array.append(sorted_array[new_index])

    # the complexity of this loop is O(n/2) since it is half of the original array aprox.
    for index, value in enumerate(number1_array):
        number1 = number1 + (10 ** index) * value
        
    # the complexity of this loop is O(n/2) since it is half of the original array aprox.
    for index, value in enumerate(number2_array):
        number2 = number2 + (10 ** index) * value
`
So we have O(n) + O(n/2) + O(n/2) = O(2n). We could approximate this to O(n)

Summing the O(n) from the counting sort O(n) plus the complexity of the three loops O(n):
 O(2n) which we could approximate to O(n)  

The space complexity is also O(n). We are using four arrays in total:
The initial array with O(n) space complexity
The count array with O(m) being m the number of different numbers in the array.
The output array with O(n) space complexity since it will store the same number of elements than in the original
array but sorted.

number1_array and number2_array which is O(n/2) since stores half of the elements approximately and its sum is O(n)

So we have in total O(n) + O(m) + O(n) + O(n/2) + O(n/2) = O(3n + m) for the space complexity.


 
 