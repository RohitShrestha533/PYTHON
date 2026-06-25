                
# subjects_list =["python","java","c++","python","javascript","java","python","java","c++","c"]

# allsub =set(subjects_list)
# print(allsub)
# lsitsub=list(allsub)
# classroom={}
# for i in range(len(lsitsub)):
#     classroom[i + 1] = lsitsub[i]

# print(classroom)



student={}
student["name"]=input("enter student name")
subjects={}
subjects["math"]=input("enter a marks obtaine in math")
subjects["IT"]=input("enter marks obtained in IT")
subjects["english"]=input("enter marks obtained in english")

student["subjects"]=subjects

print(student.items())