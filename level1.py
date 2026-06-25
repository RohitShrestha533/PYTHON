"""
Level 1: Loops & Conditions
Print numbers from 1 to 100.
Print even numbers from 1 to 100.
Find the sum of first n natural numbers.
Find the factorial of a number.
Check if a number is prime.
Count the number of digits in a number.
Reverse a number.
Check if a number is a palindrome.
Find the largest of three numbers.
Print the multiplication table of a number.
"""

even=[]
for i in range(1,101):
    # print(i, end=",")  
    if(i%2==0):
        even.append(i)

    
print(even)

n=int(input("Enter a number:"))
sum=0
factorial=1


for i in range(2,n//2+1):
    if i==2:
        print("it is prime number")
    if n%i !=0:
        print("it is prime number")




print(f'This is the digit count in a number: {len(str(n))}')
number=str(n)
print(f'This is the reverese of  a number {n}: - {number[::-1]}')

if (number == number[::-1]):
    print("it is palidrome number")
else:
    print("it is not palidrome number"  )

for i in range(1,n+1):
    sum+=i
    if i>=1:
        factorial*=i
    
print("Sum:",sum)
print("Factorial:",factorial)
print("multiple of a number {n} :\n")
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')

a,b,c = int(input("Enter a:")   ) , int(input("Enter b:")) , int(input("Enter c:"))

print(max(a,b,c))
