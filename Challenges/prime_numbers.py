import math, os

'''
Challenge I: prime numbers
THE PROBLEM
A prime number (or a prime) is a natural number greater than 1 that has
no positive divisors other than 1 and itself.
The property of being prime is called primality. A simple but slow method of
verifying the primality of a given number is known as trial division. It
consists of testing whether is a multiple of any integer between 2 and√ .
THE BASIC
Write a program that, given a number comprised between 2 and 49, returns
if it is a prime number or not. We can assume that the computer knows
(stores) that [2, 3, 5, 7] are prime numbers.
THE ADVANCED BIT
Write a program that, given a number greater than 2, returns if it is a
prime number or not. We can assume that the computer at the start knows
only that 2 is prime number. We should use a loop to test several numbers.
THE CLEVER ONE
Write a program that, given a number greater than 2, returns if it is a
prime number or not. We can assume that the computer at the start knows
only that 2 is prime number. Every time the program is ran, it should
remember the prime numbers it has found before.
THE OLYMPIAN ONE
Taken from the 2012 British Informatics Olympiad.
Every integer greater than 1 can be uniquely expressed as the product of
prime numbers (ignoring reordering those numbers). This is called the
prime factorisation of the number.
For example:
• 100 = 2 2 5 5
• 101 = 101 (since 101 is a prime number)
We are interested in the product of the distinct prime factors of a given
number; in other words each number in the prime factorisation is to be used
only once. Since 100 = 2 2 5 5 the product we require is 10 (i.e. 2
5). Write a program which reads in a single integer n (1 < n < 1,000,000)
and outputs a single integer, the product of the distinct prime factors of n.
'''

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

def isPrime(number: int) -> bool:
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

def primeFactorize(number: int) -> list:
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