def even_odd(m, n):
    for i in range(m, n + 1):
        if i % 2 == 0:
            print(i, "Even")
        else:
            print(i, "Odd")

m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))
even_odd(m, n)