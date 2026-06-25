""" Excerise on data structure of list """
my_list=[1,2,3,4,5,"apple", "banana", "cherry"]
print(my_list)
my_list[0]="rohit"
print(my_list)
my_list.append("grape")
my_list.append("orange")
print(my_list)
my_list.remove("banana")
print(my_list)
my_list.pop(2)
print(my_list)



print(my_list *3)

""" Excerise on data structure of tuple """
my_tuple=(1,2,3,4,5,"apple", "banana", "cherry")
print(my_tuple)
try:
    my_tuple[0]="rohit"
    print(my_tuple)
except TypeError as e:
    print("Error:", e)



my_dirc={
    "name":"Rohit",
    "age": 25,
    "city": "Kathmandu",
}
print(my_dirc)
my_dirc["city"]="Chitwan"
print(my_dirc)
my_dirc["country"]="Nepal"
print(my_dirc)
del my_dirc["age"]
print(my_dirc)



my_set={"apple", "banana", "cherry"}
print(my_set)
try:
    my_set.add("apple")
    print(my_set)
except TypeError as e:
    print("Error:", e)



list1=[1,2,5]
list1.insert(4,5)
print(list1)
print(list1.index(5))


n=5 

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()