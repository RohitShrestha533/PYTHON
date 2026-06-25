#Find Largest and Smallest Number
"""
Do it:
Using built-in functions.
Without using built-in functions.
"""
numbers = [23, 45, 12, 67, 89, 5]
print(f'Largest Number is : {max(numbers)}')
print(f'Smallest Number is : {min(numbers)}')


numbers.sort()
print(f'Smallest number is : {numbers[0]}')
print(f'Largest number is : {numbers[-1]}')



for i in range(len(numbers)):
    if i==0:
        largest=smallest=numbers[i]
    if numbers[i]>largest:
        largest=numbers[i]
    elif numbers[i]<smallest:
        smallest=numbers[i]

print(f'Largest number is : {largest} and Smallest number is : {smallest}')