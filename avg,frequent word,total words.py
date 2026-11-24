# Write a Python program to analyze a text file and display:  (a) total number of words,  (b) most frequently occurring word,  (c) number of unique words, and  (d) average word length
file=open("student.txt","r")
data=file.read().lower()
words=data.split()
print("total no of words:",len(words))
unique=set(words)
print(len(unique))
avg=sum(len(word) for word in words)/len(words)
print(avg)



