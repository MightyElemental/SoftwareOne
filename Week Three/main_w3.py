
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
