#!/usr/bin/python3
import os
import random
import time
import sys


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def generate_random_operator():
    operators = ['+', '-', '*', '/']
    return random.choice(operators)


N = generate_random_number(120, 180)

for _ in range(N):
    x = generate_random_number(1, 9)
    y = generate_random_number(1, 9)
    operator = generate_random_operator()

    expression = f"{x} {operator} {y}"
    print(expression)
    sys.stdout.flush()

    time.sleep(1)

os._exit(0)
