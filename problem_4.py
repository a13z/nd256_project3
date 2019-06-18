def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # variable to track the position of the 0 values
    index_0 = 0

    # variable to track the position of the 2 values
    index_2 = len(input_list) - 1

    counter_index = 0

    while counter_index <= index_2:
        print("counter_index", counter_index, "index 0", index_0, "index_2", index_2)

        if input_list[counter_index] == 0:
            input_list[counter_index] = input_list[index_0]
            input_list[index_0] = 0
            index_0 += 1
            counter_index += 1
        elif input_list[counter_index] == 2:
            input_list[counter_index] = input_list[index_2]
            input_list[index_2] = 2
            index_2 -= 1
        else:
            counter_index += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# test_function([])