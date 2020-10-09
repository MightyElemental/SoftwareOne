import math

LBS_PER_KG = 2.20462

#Q1

stones = int(input("stones> "))
pounds = int(input("pounds> "))

total_pounds = stones*14+pounds

print(stones,"stone,",pounds,"pounds is",round(total_pounds/LBS_PER_KG,1),"kilograms")

kg = int(input("KG> "))
total_pounds = LBS_PER_KG*kg
print(kg,"kilograms is",round(total_pounds/14,0),"stone",round(total_pounds%14,1),"pounds")

#Q3
def getPrice(kg):
    cost = 3*kg
    postage = 4.99
    if(cost>50):
        postage -= 1.5
    return cost+postage

kg = int(input("How many kilos of bananas? "))
print(getPrice(kg))

#Q4
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

#Q5
def heron(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

a = float(input("a> "))
b = float(input("b> "))
c = float(input("c> "))
print("area", heron(a,b,c))