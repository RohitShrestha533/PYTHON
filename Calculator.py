import sys

def calculator(cal,x,y):
    try:
        if cal == 1:
            return x + y , "Addition"
        elif cal == 2:
            return x - y , "Subtract"
        elif cal == 3:
            return x * y , "Multiply"
        elif cal == 4:
            return x / y , "Divide"
        else:
            print("Error : This calculator can only calculate +,-,*,/ ")
            sys.exit()
    except ZeroDivisionError:
        print("MathError: Cannot be divide by Zero")
    sys.exit()
    
CalcList= ["1. Addition","2. Subtract","3. Multiply","4. Divide"]

for i in CalcList:
    print(i)

try:
    calc = int(input("Choose calculation number : "))
    first = int(input("First number : "))
    second = int(input("Second number : "))
except ValueError:
    print("Error : Invalid Number")
    sys.exit()


result , calcus = calculator(calc,first,second)    
print(f" The resutant {calcus} of {first} and {second} is : {result}")