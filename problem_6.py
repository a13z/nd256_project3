def get_min_max(ints):
    """
    Function which returns a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers

    Returns:
        (int,int): tuple with the min and max values
    """
    # variables to store min and max initialised to the first element of ints array.
    min = ints[0]
    max = min

    # iterate through ints array and update min and max accordingly
    for integer in ints:
        if integer < min:
            min = integer
        elif integer > max:
            max = integer

    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


l = [i for i in range(4, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(l)
print ("Pass" if ((4, 9) == get_min_max(l)) else "Fail")