import math

LBS_PER_KG = 2.20462

# ---- Exercise 1 ----

# Write a series of small script that convert weight, distance, and liquid measurement
# from Imperial to Metric system.
# Write the reverse conversion.

stones = int(input("stones> "))
pounds = int(input("pounds> "))

total_pounds = stones*14+pounds

print(stones,"stone,",pounds,"pounds is",round(total_pounds/LBS_PER_KG,1),"kilograms")

kg = int(input("KG> "))
total_pounds = LBS_PER_KG*kg
print(kg,"kilograms is",round(total_pounds/14,0),"stone",round(total_pounds%14,1),"pounds")

# ---- Exercise 3 ----

# A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and
# packaging. If an order is over £50.00, the P&P is reduced by £1.50. Write a script that will take
# the number of kilo of bananas as a user input and print the cost of that order.
def getPrice(kg):
    cost = 3*kg
    postage = 4.99
    if(cost>50):
        postage -= 1.5
    return cost+postage

kg = int(input("How many kilos of bananas? "))
print(getPrice(kg))

# ---- Exercise 4 ----

# Write a script that take the age and rate (the heart rate) that print a description of a person's
# training zone based on his or her age and training heart rate, rate. The zone is determined
# by comparing rate with the person's maximum heart rate m:
# Interval range        |   Training Zone
# rate ≥ 0.9 m          |   Interval training
# 0.7 m ≤ rate < 0.9 m  |   Threshold training
# 0.5 m ≤ rate < 0.7 m  |   Aerobic training
# rate < 0.5 m          |   Couch potato
# The maximum heart rate in beats per minute is given by the formula: m = 208 − 0.7 * age
def getState(age,rate):
    m = 208 - 0.7*age
    if(rate > 0.9*m):
        return "Interval training"
    if(rate > 0.7*m):
        return "Threshold training"
    if(rate > 0.5*m):
        return "Aerobic training"
    return "Couch potato"

print(getState(19,120))

# ---- Exercise 5 ----

# Write a script that takes the lengths of the sides of a triangle (a, b, and c) from the user and then
# print the area of the triangle using Heron's formula. (Look up Heron's formula if you do not
# remember it.). Note, to compute x^n using Python, you must use the function pow(x,n).
def heron(a: float, b: float, c: float) -> float:
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

a = float(input("a> "))
b = float(input("b> "))
c = float(input("c> "))
print("area", heron(a,b,c))