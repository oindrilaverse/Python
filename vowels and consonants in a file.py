#)write a python program to count the numbers of vowel and consonants present in a text file
f=open("student.txt","r")
data=f.read()
vowels=0
consonants=0
for i in data:
 if i in "aeiouAEIOU" :
        vowels+=1
 else:
     consonants+=1
     print("no of vowels:", vowels)
     print("no of consonants:", consonants)