import math, os

# Challenge 1

# Ensure cache file is located next to the script for ease
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
cache_location = __location__+"/primes.cache"

prime_list = []

# Create cache if it does not exist
if not os.path.exists(cache_location):
    os.mknod(cache_location)
    prime_list = [2, 3]
else:
    f = open(cache_location, "r")
    prime_list = [int(x) for x in f.readlines()]
    f.close()

def isPrime(number: int):
    if(number <= 3):
        return number > 1
    for i in range(2, math.floor(number**0.5)):
        if(number%i==0):
            return False
    return True

def generateAndCachePrimes(upper_limit: int):
    start_pos = 3
    # Don't repeat already calculated primes
    if(len(prime_list) > 0):
        start_pos=prime_list[-1]+2
    # Skip if there is nothing to calculate
    if(upper_limit < start_pos):
        return
    # Generate prime numbers under the user's chosen number
    for i in range(start_pos, upper_limit, 2):
        if(isPrime(i)):
            prime_list.append(i)
    #print("INFO:Generated",len(prime_list),"primes")
    # Save to cache
    f = open(cache_location, "w")
    for n in prime_list:
        f.write(str(n)+"\n")
    f.close()
    #print("INFO:Cached prime numbers")

def primeFactorize(number: int):
    factor_list = []
    if(isPrime(number)):
        return [number]
    p_index = 0
    while number >= prime_list[p_index]:
        if number%prime_list[p_index] == 0:
            factor_list.append(prime_list[p_index])
            number/=prime_list[p_index]
        else:
            p_index+=1
    return factor_list

number = int(input("Enter an integer (<1,000,000) to factorize: "))
while number > 1000000:
    print("That number was larger than 1,000,000!")
    number = int(input("Enter an integer (<1,000,000) to factorize: "))

# Ensure the prime list has all primes below user's number
generateAndCachePrimes(number)

p_factors = primeFactorize(number)
if(len(p_factors) == 1):
    print("\nYour number is prime!\nIt is its only factor!")
else:
    print("\nThe prime factors of your number is", p_factors)
    print("The product of the unique numbers is", math.prod(set(p_factors)))