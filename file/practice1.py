with open("practice1.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning file I/O\n")
    f.write("using Java\n")
    f.write("I like programming in Java\n")


with open("practice1.txt","r") as f:
    data = f.read()

new_data=data.replace("Java","Python")

with open("practice1.txt","w") as f:
    f.write(new_data)
