people=[
    {"name":"ram","address":"chitwan"},
    {"name":"hari","address":"ktm"},
    {"name":"sita","address":"pkr"},
]

#people.sort(key=lambda people: people["address"])

# or we can define dunction
def func(people):
 return people["name"]
people.sort(key=func)
print(people)