import sys

sys.set_int_max_str_digits(21000)


def fibonacci(limit):
    first, second = 0, 1
    count = 1
    while count <= limit:
        yield first
        first, second = second, first + second
        count += 1


TARGETS = [5, 200, 1000, 100000]

for step, number in enumerate(fibonacci(100000), start=1):
    if step in TARGETS:
        print(number)
