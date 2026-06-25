# Word Frequency Counter

my_language =["python" ,"java" , "python" , "c++" ,"python" ,"java"]
my_dic={}

for i in range(len(my_language)):
    total=my_language.count(my_language[i])
    if my_language[i] not in my_dic.keys():
  
        my_dic[my_language[i]]=total

print(my_dic)