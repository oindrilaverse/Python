#)write a program to read a text file and display its contents in reverse order, line by line. 
file=open("student.txt","r")
lines=file.readlines()
for line in reversed(lines):
    print(line,end="")
file.close()
