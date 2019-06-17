def counting_sort(array, k):
    output = []
    count = [0 for _ in range(k+1)]

    for value in array:
        count[value] += 1

    for index, value in enumerate(count):
        output += [index] * value

    return output

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    number1_array = []
    number2_array = []
    number1 = 0
    number2 = 0

    sorted_array = counting_sort(input_list, 9)
    sorted_array_size = len(sorted_array) -1

    for index in range(sorted_array_size, -1, -1):
        new_index = sorted_array_size - index
        if new_index % 2:
            number1_array.append(sorted_array[new_index])
        else:
            number2_array.append(sorted_array[new_index])

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
