#write a program to search for a particular word in a text file and display only those lines containing given keyword
f=open("student.txt","r")
data=f.read().lower()
word=input("enter the word to search: ").lower()
lines=data.splitlines()
count=0
for line in lines:
    if word in line:
        count+=1
    else:
        pass
    f.close()
print("Number of lines containing the word:", count)