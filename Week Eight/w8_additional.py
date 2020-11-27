#Week 8 – Additional Exercises

# ---- Exercise 1 ----
'''
1. Write a recursive function print_all(numbers) that prints all the
elements of list of integers, one per line (use no while loops or for loops).
The parameters numbers to the function is a list of int.
2. Same problem as the last one but prints out the elements in reverse order.
'''

def print_all(numbers: list):
    if len(numbers) == 0: return
    print(numbers[0])
    print_all(numbers[1:])

#print_all([1,2,3,4,5])

def print_all_reverse(numbers: list):
    if len(numbers) == 0: return
    print(numbers[-1])
    print_all_reverse(numbers[:-1])

#print_all_reverse([1,2,3,4,5])

# ---- Exercise 2 ----
'''
There is an elegant algorithm for converting a decimal number to a binary number. You need
to carry out long division by 2 to use this algorithm. If we want to convert 8310 to binary, then
we can repeatedly perform long division by 2 on the quotient of each result until the quotient
is zero. Then, the string of the remainders that were accumulated while dividing make up the
binary number. For example,

83/2 = 41 remainder 1
41/2 = 20 remainder 1
20/2 = 10 remainder 0
10/2 = 5 remainder 0
5/2 = 2 remainder 1
2/2 = 1 remainder 0
1/2 = 0 remainder 1

The remainders from last to first are 1010011(2) which is 83(10).
a) Implement a recursive function to_binary(number) that takes a positive integer
as parameter and returns a binary representation of that number as a string.
b) Implement the reverse function to_base10(binary) that takes a string containing
a binary number and returns its representation in base 10. The function must be
recursive. To test your solution once implemented to_base10(to_binary(83))
should return 83.
'''

def to_binary(number:int)->str:
    if number == 0: return ""
    return to_binary(number//2) + str(number%2)

#print(to_binary(83))
    
def to_base10(binary):
    if len(binary) == 0: return 0
    return 2 * to_base10(binary[:-1]) + int(binary[-1])

#print(to_base10(str(to_binary(83))))

# ---- Exercise 3 ----
'''
We are given a set of items, each with a weight and a value and we need to determine the
number of each item to include in a collection (a bag for example) so that the total weight is
less than or equal to a given limit and the total value is as large as possible. In addition, the
items are indivisible; we can either take an item or not. Note that there might be more than one
item with same value and same weight. For example,

Input:
value = [20, 5, 5, 10, 40, 15, 25]
weight = [1, 2, 2, 3, 8, 7, 4]
max_weight = 10

Output: 60
value = 20 + 40 = 60
weight = 1 + 8 = 9

The idea is to use recursion to solve this problem. For each item, there are two possibilities
1. We include current item in the bag and recur for remaining items with decreased
capacity of the bag. If the capacity becomes negative, do not recur or return -INFINITY.
2. We exclude current item from the bag and recur for remaining items
Finally, we return maximum value we get by including or excluding current item. The base
case of the recursion would be when no items are left, or capacity becomes 0.

Naïve Implementation:
Implement a naïve implementation that try all possible solution and returns the maximum.
'''

def collect_item(values, weights, capacity):
    if capacity < 0: return -9999999
    if len(values) == 0 or capacity == 0: return 0
    temp = []
    for i in range(len(values)):
        t_values = values.copy()
        del t_values[i]
        t_weight = weights.copy()
        del t_weight[i]
        temp.append(values[i]+collect_item(t_values, t_weight, capacity - weights[i]))
    return max(temp)

value = [20, 5, 5, 10, 40, 15, 25]
weight = [1, 2, 2, 3, 8, 7, 4]
max_weight = 10

print(collect_item(value, weight, max_weight))