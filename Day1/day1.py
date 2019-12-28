import math
file = open('./input.txt','r')

def calculateFuel(mass):
    return math.floor(mass/3)-2

def getTotalFuel(rockets):
    totalfuel = 0
    for mass in rockets:
        fuelToAdd = calculateFuel(int(mass))
        while fuelToAdd > 0:
            totalfuel = totalfuel+fuelToAdd
            fuelToAdd = calculateFuel(fuelToAdd)
    return totalfuel


print(getTotalFuel(file))