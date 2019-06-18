
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Base cases so we could create a candidates array half size.
    if number < 0:
        return None

    # Lower and upper bounds to start binary search
    lower_bound = 0
    upper_bound = number
    # Variables to store the latest lower and upper bounds which we compare at the end to get the floored square root
    latest_lobound = 0
    latest_upbound = 0

    # We iterate while lower bound is not higher than upper bound
    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        power_of_two = midpoint * midpoint
        if power_of_two == number:
            return midpoint
        elif power_of_two > number:
            latest_upbound = midpoint
            upper_bound = midpoint - 1
        else:
            latest_lobound = midpoint
            lower_bound = midpoint + 1

    if latest_upbound * latest_upbound > number:
        return latest_lobound
    else:
        return latest_upbound

def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]
    print(sqrt(number), solution)
    if sqrt(number) == solution:
        print("Pass")
    else:
        print("Fail")

test_function((30, 5))
test_function((9, 3))
test_function((0, 0))
test_function((16, 4))
test_function((1, 1))
test_function((27, 5))
test_function((-5, None))