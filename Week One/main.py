import math

#Q1

stones = int(input("stones> "))
pounds = int(input("pounds> "))

print("")

#Q3
def getPrice(kg):
    cost = 3*kg
    postage = 4.99
    if(cost>50):
        postage -= 1.5
    return cost+postage

print(getPrice(1))

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