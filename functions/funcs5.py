def summ(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b



def calculator(a, b, c = "+"):
    if c == "+":
        return summ(a, b)
    elif c == "-":
        return subtraction(a, b)
    elif c == "*":
        return multiplication(a, b)
    elif c == "/":
        return division(a, b)



print(calculator(3, 2, "/"))