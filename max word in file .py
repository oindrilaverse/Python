#)write a python program to find the longest word in a text file 
f=open("student.txt","r")
data=f.read()
words=data.split()
longest=max(words,key=len)
print("longest word:",longest)