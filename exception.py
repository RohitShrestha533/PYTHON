import sys # for exit and show exception error
try:
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError:
    print("invalid input")
    sys.exit()

try:
    result = x / y
except ZeroDivisionError:
    print("error cannot divide by 0")
    sys.exit()

print(f"{x} / {y} is : {result}")