#rite a program in Python to print 1st n numbers of a Fibonacci series. (Get the value of n from User)  In Fibonacci series, next number is the sum of previous two numbers, and the first two numbers of Fibonacci series are 0 and 1.  Example: First 9 numbers of the Fibonacci series are as follows:  0, 1, 1, 2, 3, 5, 8, 13, 21
def fibo(n):
    a=0
    b=1
    for i in range(n):
       print(a,end="")
       c=a+b
       a=b
       b=c
n=int(input("enter range:"))
     
print("fibonacci series:")
fibo(n)
    