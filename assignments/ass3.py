#Take a string from the user and print it reversed.

text=str(input("Enter any string: "))
print(text[::-1])
a = "Kathmandu"
vowels = "aeiou"

count = sum(map(a.lower().count, vowels))

print(count)