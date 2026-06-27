with open("practice2.txt","r") as f:
    data =f.read()


# number=list(int(data.split(",")))
number=list(data.split(","))
count=0
for i in number:
    if int(i)%2==0:
        count+=1


print(count)