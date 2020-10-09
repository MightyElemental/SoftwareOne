import math, re
# E1
# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
# Write a program to keep asking for a number until you enter a negative number. At the end, print the average of all entered numbers.
# Write a program to keep asking for a number until you enter a negative number. At the end, print the number of even number entered.
sum = 0
num = float(input("Enter a number> "))
entry_count = 0
sum += num
while(num >= 0):
    num = float(input("Enter a number> "))
    entry_count += 1
    sum+=num
print("You entered",entry_count,"numbers")
print("The total of the numbers you entered is:",sum)
print("So the average is",round(sum/entry_count,1),"to 1 d.p.")

# ---- PRACTICAL ----

# Write a program that take a sentence or a word as an input and print if it is a palindrome or not.
# ‘Dammit, I'm mad!’ is also considered a palindrome when neither punctuation nor spaces are taken into account.
# Change your program so it can recognise these palindromes too.
phrase = input("Enter a phrase> ").lower()
phrase = re.sub("[^a-z]","", phrase) # use regex to remove any non-letter
flag = False
for i in range(math.ceil(len(phrase)/2)):
    s_letter = phrase[i]
    e_letter = phrase[len(phrase)-1-i]
    if(s_letter != e_letter):
        flag = True
        break
if(flag):
    print("This is NOT palindromic")
else:
    print("This IS palindromic")
