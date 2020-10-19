# WEEK 4 - PRACTICAL 3

# ---- Exercise 1 ----
'''
Write a function sum_digits(number) to calculate and return the sum of the digits of a
given whole number (int) given as parameter. For example:
>>> print(sum_digits(1234))
10
'''

# Convert int to a list of digits then sum the list
def sum_digits(number: int) -> int:
    digit_list = [int(d) for d in str(number)]
    result = sum(digit_list)
    return result

print("---")
print(sum_digits(1234))

# ---- Exercise 2 ----
'''
Write a function pairwise_digits(number_a, number_b) that take two integer as
parameters and a binary string where a character 1 is used if the digits at the same index are
the same, a 0 otherwise. Examples are given in the table below.
+---------+---------+---------+
| Input A | Input B | Output  |
+=========+=========+=========+
| 1213    | 2113    | '0011'  |
+---------+---------+---------+
| 1213    | 10435   | '10010' |
+---------+---------+---------+
| 1213    | 121     | '1110'  |
+---------+---------+---------+
'''

def pairwise_digits(number_a: int, number_b: int) -> str:
    a_lst  = [d for d in str(number_a)]
    b_lst  = [d for d in str(number_b)]
    result = ""
    for x in range(0,max(len(a_lst),len(b_lst))):
        if(x >= len(a_lst) or x >= len(b_lst)):
            result += "0"
            continue
        if(a_lst[x]==b_lst[x]):
            result += "1"
        else:
            result += "0"
    return result

print("---")
print(pairwise_digits(1213, 2113))  # 0011
print(pairwise_digits(1213, 10435)) # 10010
print(pairwise_digits(1213, 121))   # 1110

# ---- Exercise 3 ----
'''
Write a function to_base10(binary) that take a binary number (base 2), convert it into
a decimal number (base 10) and return the base 10 value. To compute such a value, we need to
understand what a binary number is.
!<The question explains binary but I'm not including the table here>!
The binary number 10001011 represents the number 139, whereas the number 11111111
represents 255
'''

# Python already has built in functionality for this.
# e.g. 0b10001011 = 139

def to_base10(binary: int) -> int:
    digit_list = [int(d) for d in str(binary)]
    digits = len(digit_list)
    denary_num = sum([digit_list[x]*(2**(digits-x-1)) for x in range(0,digits)])
    return denary_num

print("---")
print(to_base10(10001011)) # 139
print(to_base10(11111111)) # 255
print(to_base10(00000000)) # 0
print(to_base10(10101010)) # 170

# ---- Exercise 4 ----
'''
Write a python script to print the Floyd’s Triangle. For example:
>>> Input number of rows: 5
1
01
101
0101
10101
'''

def floyds_triangle(rows: int):
    current_row = ""
    for i in range(rows):
        current_row = str((i+1)%2)+current_row
        print(current_row)

print("---")
floyds_triangle(5)

# ---- Exercise 5 ----
'''
You have just started your placement, and you are given a piece of code to correct. The aim of
the script is to take a 2D list (that is a list of lists) and print a list containing the sum of each
list. For example, given the list in data, the output should be [6, 2, 10].
Modify the code below such that it gives the right result. In addition, you have been asked to
refactor the script into a function sum_lists(list_2D) that returns the list containing the
sums of each sub-list.

    data = [[1,2,3], [2], [1, 2, 3, 4]]
    output =[]
    total = 0
    for row in data:
        for val in row:
            total += val
            output.append(total)
    print(output)
'''

def sum_lists(list_2D: list) -> list:
    output = []
    for row in data:
        output.append(sum(row))
    return output

data = [
    [1, 2, 3], 
    [2],
    [1, 2, 3, 4]
]

print("---")
print(sum_lists(data)) # [6, 2, 10]