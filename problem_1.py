
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Base cases so we could create a candidates array half size.
    if number <= 0:
        return 0
    if number == 1:
        return 1

    # candidates is an array with numbers from 0 to number // 2
    # they will be potential candidates to be the square root of number
    candidates = [i for i in range(0, number//2)]

    # Binary search required variables to shrink the array in half
    midpoint = 0
    lower_bound = 0
    upper_bound = len(candidates) - 1


    # Traverse the candidates array in halves while the lower_bound is not higher than the upper_bound
    # divide the array in half based if the candidate power of two is higher or lower than the number
    # We discard the candidates which power of two are higher than the number and we iterate until
    # bounds are crossed. That way we get the candidate closest to the square root of number
    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        candidate_power_two = candidates[midpoint] * candidates[midpoint]
        if candidate_power_two == number:
            return candidates[midpoint]
        if candidate_power_two > number:
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1

    return candidates[midpoint]


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    if sqrt(number) == solution:
        print("Pass")
    else:
        print("Fail")

test_function((9, 3))
test_function((0, 0))
test_function((16, 4))
test_function((1, 1))
test_function((27, 5))
test_function((-5, 0))