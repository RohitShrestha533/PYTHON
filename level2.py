"""
Level 2: Functions
Write a function to add two numbers.
Write a function to find the square of a number.
Write a function to check whether a number is even or odd.
Write a function to find the maximum of two numbers.
Write a function to calculate factorial.
Write a function to check prime numbers.
Write a function to calculate the sum of digits.
Write a function to reverse a number.
Write a function to count vowels in a string.
Write a function to check palindrome strings.
"""

def add_two_number(a,b):
    return a+b


def square_number(a):
    return a**2

def even_odd(a):
    if(a%2==0):
        print(f'number {a} is a even number')
    else:
        print(f'number {a} is a odd number')

def maximun_number(a,b):
    if a>b:
        print(f' Number {a} is maximun_number')
    if(b>a):
        print(f' Number {b} is maximun_number')

    if(a==b):
        print(f' Number {a} and {b} are same number')

def factorial(a):

    if a==0 or a==1:
        return 1

    return a* factorial(a-1)

def prime_number(a):
    if a<2:
        print("not a prime number")
        exit()
    for i in range(2,a//2+1):
        if a%i ==0:
            print(f'Not a prime number')
            return False

    print(f'Number {a} is a prime number' )
    return True

def sum_of_digit(a):
    length=len(str(a))
    sum_of_digit=0
    for i in range(length):
        sum_of_digit+=int(str(a)[i])
    print(f'The sum of digits of a number is : {sum_of_digit}')


def reverse_number(a):
    num=str(a)
    return(int(num[::-1]))


def count_vowels( a):
    count_vowels=0
    word=a.lower()

    for letter in word:
        if letter in "aeiou":
            count_vowels+=1


def palindrome(a):
    for i in range(len(a)//2):
        j=len(a)-i-1
        if a[i]!=a[j]:
            print(f'This string isnot a palindrome ')
            return False
    print(f'The string {a} is a palindrome')
    return True

