f =open("text.txt","r")
data=f.read()
print(data)
f.close()


w =open("text.txt","w")
w.write("hello")
w.close()

a =open("text.txt","a")
a.write("\ni will be leairng python")
a.close()

