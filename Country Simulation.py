import random
startpopulation = int(input("Start Population:"))
yearstobesimulated = int(input("Years To Be Simulated:"))
deathrateperyear = int(input("Additional Death Rate:"))
includerandomdeathrateperyear = input("Include Random Death Rate Per Year? Y Or N:")
print("Simulating")
highestpopulation = int(0)
population = startpopulation
totaldeaths = int(0)
for x in range(0, yearstobesimulated):
    for x in range(2):
        population = population + random.randint(0, 10)
        population = population - 2
        totaldeaths = totaldeaths + 2
        if population > highestpopulation:
            highestpopulation = population
    if includerandomdeathrateperyear == ("Y"):
        deathrateperyear = random.randint(10, 50)
    population = population - deathrateperyear
    totaldeaths = totaldeaths + deathrateperyear
print("Done")
print("Results")
print("Highest Population In Simulation:")
print(highestpopulation)
print("Total Deaths:")
print(totaldeaths)