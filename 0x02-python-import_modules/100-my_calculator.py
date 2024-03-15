#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    num = len(argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if op == '+':
        print(f"{a} {op} {b} = {add(a, b}}")
    elif op == '-':
        print(f"{a} {op} {b} = {sub(a, b)}")
    elif op == '*':
        print(f"{a} {op} {b} = {mul(a, b)}")
    elif op == '/':
        print(f"{a} {op} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
