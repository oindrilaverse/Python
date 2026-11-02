
#1. a, b, c = 1, 2, 3; Reassign so that a=3, b=1, c=2

a,b,c=1,2,3
print(a,b,c)

#data = [10, 20, 30, 40, 50]; Assign first element to x, last element to y, middle ones to z
data=[10,20,30,40,50]
x,*z,y=data
print(x,y,z)


#3. x, y, z = 5, 10, 15;  Rotate so that x=10, y=15, z=5
x,y,z= 5,10,15
x,y,z= z,y,x
print(x,y,z)



#4. word = "ABC"; Assign 'A' to a, 'B' to b, 'C' to c
word="ABC"
a,b,c=word
print(a,b,c)



#5. Convert '45.6' into integer.
a=int(float('45.6'))
print(a)



#6. marks = [95, 87, 76, 88, 92]; Store only the first and last marks, ignore others
marks=[95, 87, 76, 88, 92]
x,*_,y=marks
print(x,y)


#7. What happens if you cast: float("1.2e3")

a=float('1.2e3')
print(a)
#output:1200 

#8. student = ['Alice', 21, 'CSE'], print name, age and branch
student = ['Alice', 21, 'CSE']
name,age,branch=student
print(name,age,branch)

#10. convert 5 into complex form.
result= complex(5)
print(result)
#Output:(5+0j)

#9. What will be the result of int("True") and int(True)
print(int("True"))
print(int(True))
#int(True) returns 1 because booleans are a subclass of integers in Python.
# int("True") raises a ValueError because the text string "True" does not contain numerical digit


