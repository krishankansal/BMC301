# to find the factors of a given number

x=int(input("Enter a number: "))

for i in range(1,x+1):
    if x%i==0:
        print(i, end=" ")




