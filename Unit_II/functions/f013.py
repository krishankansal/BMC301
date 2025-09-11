# prime number -- only factors are 1 and itself
# factors(17) is [1, 17]
# factors(18) is [1,2,3,6,9,18]

from l import *

def isprime(n):
    if factors(n) == [1, n]:
        return True
        #print(n,"is prime number")
    else:
        return False
        #print(n,"is not a prime number")


if __name__ == "__main__":
    print(isprime(13))
    # print(isprime(100))
    # print(type(isprime)) # <class 'function'>
    # print(type(isprime(13))) # <class 'bool'>








