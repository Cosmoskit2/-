# import random
#
# def is_odd(numm):
#     if numm % 2 != 1:
#         return True
#     else:
#         return False
#
# def random_is_odd(n):
#     random_numbers = {"odd": 0, "even": 0}
#     for i in range(n):
#         number = random.randint(1, 1000)
#         if is_odd(number) == True:
#             random_numbers["odd"] += 1
#         else:
#             random_numbers["even"] += 1
#     return random_numbers
#
# random_is_odd(10)
#
#
# def multiple(*args):
#     a = 1
#     for i in args:
#         a *= i
#     print(args)
#     return a
#
# print(multiple(2, 3, 5))

def process_order(*args, name, surname):
    print("Продукты:", *args)
    print("Информация:")
    print("name:", name)
    print("surname:", surname)

process_order('Пицца', 'Суши', name='Райан', surname='Гослинг')

# def summ(a, b):
#     return a + b
#
# def subtraction(a, b):
#     return a - b
#
# def multiplication(a, b):
#     return a * b
#
# def division(a, b):
#     return a / b
#
#
#
# def calculator(a, b, c = "+"):
#     if c == "+":
#         return summ(a, b)
#     elif c == "-":
#         return subtraction(a, b)
#     elif c == "*":
#         return multiplication(a, b)
#     elif c == "/":
#         return division(a, b)
#
#
#
# print(calculator(3, 2, "/"))