import math, re
# Exercise 1
# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
# Write a program to keep asking for a number until you enter a negative number. At the end, print the average of all entered numbers.
# Write a program to keep asking for a number until you enter a negative number. At the end, print the number of even number entered.
sum = 0
num = float(input("Enter a number> "))
entry_count = 0
while(num >= 0):
    sum+=num
    num = float(input("Enter a number> "))
    entry_count += 1
print("You entered",entry_count,"numbers")
print("The total of the numbers you entered is:",sum)
print("So the average is",round(sum/entry_count,1),"to 1 d.p.")

# ---- PRACTICAL ----

# ---- Exercise 1 ----

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

# ---- Exercise 2 ----

# Write a script that takes a sentence from the user without any punctuation and prints
# the sentence without any white spaces. Note a white space is represented by ' ', and
# an empty string is represented by ''.
print(re.sub(r"\s", "", input("Enter a sentence> ")))

# Same as above except that each word in the output should start with a upper case letter
# and all other letter should be lower case (also known as CamelCase).
print(re.sub(r"(\b[a-z])", lambda x : x.group(1).upper(), input("Enter a sentence> ").lower()))

# Write a script that takes a sentence from a user written in CamelCase (without any blank
# spaces), creates the list of words from that sentence, and then prints that list.
# Example input: ThisIsACamelCaseSentenceWithNoSpaces
print(re.findall(r"([A-Z].*?)(?=[A-Z]|$)", input("Enter a sentence> ")))

# ---- Exercise 3 ----

# Write a script that encrypts a plain text into a cypher text using the Caesar Cipher algorithm.
phrase = input("Enter a message> ").lower()
shift_raw = input("a=").lower()
shift = ord(shift_raw)-97
encrypted_phrase = ""
for l in phrase:
    if(l == " "): # don't encrypt spaces
        encrypted_phrase += " "
        continue
    # shift to a=0, then add shift, then ensure it's within 26 letter limit, then shift to a=97
    letter_value = ( ( ord(l) - 97 ) + shift ) % 26 + 97
    encrypted_phrase += chr(letter_value)
print("Encrypted message:")
print(encrypted_phrase)

# Write a script that decrypts a cipher text into a plain text using the Caesar Cipher algorithm.
phrase = input("Enter an encrypted message> ").lower()
shift_raw = input("a=").lower()
shift = ord(shift_raw)-97
decrypted_phrase = ""
for l in phrase:
    if(l == " "): # don't decrypt spaces
        decrypted_phrase += " "
        continue
    # shift to a=0, then sub shift, then ensure it's within 26 letter limit, then shift to a=97
    letter_value = ( ( ord(l) - 97 ) - shift ) % 26 + 97
    decrypted_phrase += chr(letter_value)
print("Decrypted message:")
print(decrypted_phrase)