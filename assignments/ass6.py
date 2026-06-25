#Remove duplicates and print unique values.
items = [1,2,3,2,4,5,1,6,3]
print(set(items))
""" Tuple Practice
Print first item.
Print last item.
Find index of "blue".
Count total elements.
"""
colors = ("red", "green", "blue", "yellow")
print(colors[0])
print(colors[-1])
print(colors.index("yellow"))
print(len(colors))


"""
Tasks: Dictionary Practice

Print all keys.
Print all values.
Add GPA.
Update age.
Delete faculty.
Check if GPA exists.
"""

student = {
    "name": "Rohit",
    "age": 22,
    "faculty": "BCIS"
}

print(student.keys())
print(student.values())
student["GPA"]=3.76
print(student)
student["age"]=25
print(student)
student.pop("faculty")
print(student)

if "GPA" in student:
    print("YES")

print(student["GPA"])