import random

def is_odd(numm):
    if numm % 2 != 1:
        return True
    else:
        return False

def random_is_odd(n):
    random_numbers = {"odd": 0, "even": 0}
    for i in range(n):
        number = random.randint(1, 1000)
        if is_odd(number) == True:
            random_numbers["odd"] += 1
        else:
            random_numbers["even"] += 1
    return random_numbers

print(random_is_odd(10))

