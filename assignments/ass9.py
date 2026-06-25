"""
Student Marks System
Store marks of 5 subjects in a dictionary.

Calculate:

Total marks
Average marks
Highest scoring subject
Lowest scoring subject
"""

mark={
    "Math": 80,
    "English": 70,
    "Science": 90,
    "computer": 98,
    "nepali": 60,
}
maximum=0
total=0
first=True
for subject,score in mark.items():
    total+=score

    if first:
        maximum=score
        minimum=score
        maximum_sub=subject
        minimum_sub=subject
        first=False
    if score > maximum:
        maximum=score
        maximum_sub=subject
    if score < minimum:
        minimum=score
        minimum_sub=subject
        

print(total)
print(total/(len(mark)))
print(f'highest subject ${maximum_sub} marks is ${maximum}')
print(f'lowest subject ${minimum_sub} marks is ${minimum}')
