# add
def add(n1, n2):
    return n1 + n2


# subtract
def sub(n1, n2):
    return n1 - n2


# multiplication
def multiply(n1, n2):
    return n1 * n2


# division
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": multiply, "/": divide}


def calculator(num1: int, num2: int, operator: str) -> int:
    if operator in operations:
        function = operations[operator]
        return function(num1, num2)


print(calculator(20, 10, "+"))
print(calculator(20, 10, "-"))
print(calculator(20, 10, "*"))
print(calculator(20, 10, "/"))
