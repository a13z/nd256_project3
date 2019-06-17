def counting_sort(array, k):
    """
    Function to implement the counting sort algorithm.
    https://en.wikipedia.org/wiki/Counting_sort

    Args:
       array(Array), k(int): unsorted array, k is the range of different values in the array
    Returns:
       output(Array): this is the array sorted in ascending order.
    """
    output = []
    # count array will stores the number of times a number appears in an array
    count = [0 for _ in range(k+1)]

    # iterate through the array and count the number of times a number appears in the array
    # and stores them in the count array
    for number in array:
        count[number] += 1

    # iterate through count array and add a number as many times as appeared in the original array
    # but in ascending order
    for number, times in enumerate(count):
        output += [number] * times

    return output

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Arrays and variables to store the numbers required
    number1_array = []
    number2_array = []
    number1 = 0
    number2 = 0

    # sort the input_list array and store it in sorted_array. 9 is the range given in the
    # description of the problem, range(0, 9)
    sorted_array = counting_sort(input_list, 9)

    sorted_array_size = len(sorted_array) -1

    # iterate through the sorted_array and based on its index, starting from the end of the array,
    # assign the numbers with even index to number1_array and the odd index's numbers to number2_array
    for index in range(sorted_array_size, -1, -1):
        new_index = sorted_array_size - index
        if new_index % 2:
            number1_array.append(sorted_array[new_index])
        else:
            number2_array.append(sorted_array[new_index])

    # Convert the number1_array and number2_array into integer numbers taking their index as
    # power of 10. i.e. index 0, would be 10 * 0, index 1 -> 10 * 1 and so on
    for index, value in enumerate(number1_array):
        number1 = number1 + (10 ** index) * value

    for index, value in enumerate(number2_array):
        number2 = number2 + (10 ** index) * value

    return [number1, number2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case = ([[1, 2, 3, 4, 5], [542, 31]])
test_function(test_case)

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[0, 0, 0, 0, 0], [0, 0]]
test_function(test_case)
