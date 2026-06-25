# Write a recursive function to calculate the sum of first n natural numbers.


def sum_nth_term(n):
    if (n==1 ):
        return 1
    else:
        return n+sum_nth_term(n-1)
num = int(input("Enter the number up to where you want the sum : \n"))
print(sum_nth_term(num))

total=0
for i in range(1,num+1):
    total+=i

print(total)