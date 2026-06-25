people=[
    {"name":"ram","address":"chitwan"},
    {"name":"hari","address":"ktm"},
    {"name":"sita","address":"pkr"},
]

#people.sort(key=lambda people: people["address"])

# # or we can define dunction
# def func(people):
#  return people["name"]
# people.sort(key=func)
# print(people)


volume =lambda l,b,h :l*b*h;
print(volume(10,20,30))

def check(n):
    r=n%3
    if r==0:
        return n


number=list(range(1,11))
print(list(map(check,number)))
print(list(filter(check,number)))