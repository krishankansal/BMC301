# find all the factors of number n
# as we know factors lie's between 1 and n

def factors(n):
    fact_list = []
    for i in range(1, n+1):
        if n % i == 0:
            fact_list = fact_list + [i]

    return(fact_list)

if __name__ == "__main__":
    print(factors(22))



