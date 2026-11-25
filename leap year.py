def leap_year(n):
    if n%400==0:
             print(n,"is leap year")
    elif n%100==0:
             print(n,"is leap year")
    elif n%4==0:
            print(n,"is leap year")
    else:
            print("not")
n=int(input("enter year:"))
leap_year(n)
