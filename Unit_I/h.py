# To find whether a given number is prime or not
l=list()
num = int(input("Enter a number: "))
for i in range(1,num+1):
    if num%i==0:
        l.append(i)
print(l)
if len(l) == 2:
    print(f"Number {num} is Prime")
else:
    print(f"Number {num} is Not Prime")




