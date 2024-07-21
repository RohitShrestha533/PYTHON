# for import function from other file :from filename import function_name
number=int(input("Enter number : "))
print(f"The number is : {number}")

if number%2==0:
    print("its an even number")
else:
    print("its an odd number")

name="Rohit"
print(name[0])    #the first charcter will be print
list=["Ram","Hari"]
print(list) #whole lists
print(list[0][1]) #first value's second index(1)
list.append("sita")
print(list)
list.sort()
print(list)

#define set
set=set()
#add item in set
set.add(8)
set.add(8) #doesnot add repeated items
set.add(2)
set.add(3)
set.remove(3)
print(set)

print(f"the length of set is : {len(set) }")

#loops
for i in [0,1,2,3,4,5]:
    print(i)

for i in range(3):
    print(i)    

for c in name:
    print(c)

#dictionaries
dic={"John":"BCIS","Cena":"BBA"}
print(dic["John"])    #print john's value

#define function
def square(x):
    return x*x

for i in range(10):
    print(f"The square of {i} is :{square(i)}")