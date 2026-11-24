#Write a Python program to copy the contents of one text file into another file.
f=open("student.txt","r")
data=f.read()
f.close()
f=open("new_student.txt","w")
f.write(data)
f.close()
