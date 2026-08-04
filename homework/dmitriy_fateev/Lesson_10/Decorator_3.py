def calculating(func):
    def wrapper(first, second):

        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        else:
            operation = "/"
        return func(first, second, operation)

    return wrapper


@calculating
def calc(first, second, operation):

    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "/":
        return first / second
    return first * second


print(calc(2, 4))
