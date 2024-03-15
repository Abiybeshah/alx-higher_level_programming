#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    num = len(argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    i = int(argv[1])
    op = argv[2]
    j = int(argv[3])
    if op == '+':
        print(f"{i} {op} {j} = {add(a, b)}")
    elif op == '-':
        print(f"{i} {op} {j} = {sub(a, b)}")
    elif op == '*':
        print(f"{i} {op} {j} = {mul(a, b)}")
    elif op == '/':
        print(f"{i} {op} {j} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
