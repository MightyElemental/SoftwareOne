# ---- Exercise 1 ----

# Write a script asking the user to enter a series of positive integers separated by a white
# space, and then prints the number of even numbers that was entered. For example:
# >>> enter a series of numbers: 1 2 4 3 6 8 5 2 11 100 101
# There are 6 even numbers
numbers = input("Enter a series of positive numbers: ")
num_list = numbers.split(" ") # re.findall(r"(\d+)",numbers)
even_numbers = []
for n in num_list:
    if(int(n)%2==0):
        even_numbers.append(int(n))
print("You typed",len(even_numbers),"even numbers")

# Same question except we would like to have the list of even number as well
print("Here is the list of even numbers:",even_numbers)

# Same question except we would like to have the list of even number without duplicate,
# that is remove the second 2 in the example below.
print("Here is the set of distinct even numbers:",set(even_numbers))

# ---- Exercise 2 ----

# Write a script that asks a user to enter 4 digits (comprised between 0 and 4) separated
# by a white space, the store each digit in a list and print the list.
def getFourDigits():
    digits_raw = input("Enter 4 digits (0..4) separated by a space: ")
    digits = [int(x) for x in digits_raw.split(" ")]
    return digits

# Write a script that ask a user to enter 4 times a sequence of 4 digits, and store it in a 2D
# list, that is a list containing 4 lists of 4 digits each. The script should print the 2D list.
list_2d = [getFourDigits() for i in range(4)]
print(list_2d)

# Modify your script so the output is formatted in a table
# Modify your script so the 0 are replaced by a blank space
print("+-+-+-+-+")
for x in range(len(list_2d)):
    print("|","|".join(map(str,list_2d[x])).replace("0"," "),"|", sep="")
    print("+-+-+-+-+")

# ---- Exercise 3 ----

# Write a script that takes a positive decmial integer and converts it to binary
start_num = int(input("Enter a positive decmial integer> "))
num = start_num
# print(num,"in binary is",bin(num).replace("0b",""))
bin_str = ""
while(num > 0):
    bin_str=str(num%2)+bin_str
    num//=2
print(start_num,"in binary is",bin_str)