#write a python program to create a text file named student.txt and write student details into it

file=open("student.txt","w")
name=input("enter name:")
roll=input("enter roll:")
file.write(name+"\n")
file.write(roll+"\n")
print("data created")
file.close()