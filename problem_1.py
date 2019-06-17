
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number <= 0:
        return 0

    if number == 1:
        return 1

    candidates = [i for i in range(0, number//2)]
    midpoint = 0
    lower_bound = 0
    upper_bound = len(candidates) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        candidate_result = candidates[midpoint] * candidates[midpoint]
        if candidate_result == number:
            return candidates[midpoint]
        if candidate_result > number:
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