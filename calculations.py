value = 0  # The first value in the equation
operation = ""  # This is the operation that will be happening.
othervalue = 0  # This is the second value in the equation.
series = "0"  # This is a string of the whole equation


def get_value():
    """
    This function just outputs what the current value for the first number is
    :return: The first value is returned here
    """
    global value
    return value


def clear(optional=0):
    """
    This function resets the operator and 2nd value to their original state that is displayed at the top of the code
    :param optional: Changing this will change the first value in the equation
    :return: The new first value of the equation is return, this is what was inputted
    """
    global value
    global operation
    global othervalue
    global series
    operation = ""
    othervalue = 0
    value = optional
    series = str(optional)
    return optional


def step(operator, number):
    """
    This function performs an equation by putting in the operator and 2nd value
    :param operator: This is the operator (ex. +, -, *, //)
    :param number: This is the second value in the equation
    :return: What is return is what was gotten from the equation
    """
    global value
    global operation
    global othervalue
    global series
    operation = operator  # Setting the global value to the inputted one
    othervalue = number  # Same here as above
    if operation == "+":  # This conducts addition
        series = ("(" + series + ")" + operation + str(othervalue))  # This updates the series, it's in all conditions
        value += othervalue
    elif operation == "-":  # This conducts subtraction
        series = ("(" + series + ")" + operation + str(othervalue))
        value -= othervalue
    elif operation == "*":  # This conducts multiplication
        series = ("(" + series + ")" + operation + str(othervalue))
        value *= othervalue
    elif operation == "//":  # This conducts division
        series = ("(" + series + ")" + operation + str(othervalue))
        value //= othervalue
    return value


def repeat():
    """
    This function just repeats the last operation that occurred again.
    :return: This is the value obtained after repeating operation again.
    """
    global value
    global operation
    global othervalue
    global series
    if operation == "+":  # This conducts addition
        series = ("(" + series + ")" + operation + str(othervalue))  # This updates the series, it's in all conditions
        value += othervalue
    elif operation == "-":  # This conducts subtraction
        series = ("(" + series + ")" + operation + str(othervalue))
        value -= othervalue
    elif operation == "*":  # This conducts multiplication
        series = ("(" + series + ")" + operation + str(othervalue))
        value *= othervalue
    elif operation == "//":  # This conducts division
        series = ("(" + series + ")" + operation + str(othervalue))
        value //= othervalue
    return value


def get_expr():
    """
    This function just returns what series' value is, so it can print it
    :return: The expression of the equation is returned
    """
    global series
    return series
