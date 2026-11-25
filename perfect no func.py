#2) Write a program in Python, which will check a given number is perfect number or not. ( A number is called perfect when sum of all its factors, except itself, is equal to the number, i.e. 6 is a perfect number, 6=1+2+3, factors of 6=(1,2,3)). 
def perfect(n):
    sum=0
    for i in range (1,n):
    
        if n%i==0:
             sum=sum+i

    if sum==n:
             print("perfect number")
    else:
             print("not")


n=int(input("enter no:"))

perfect(n)
