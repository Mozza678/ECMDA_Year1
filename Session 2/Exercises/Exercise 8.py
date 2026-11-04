TimesForTenOscillations = []
SumOfPeriods = 0

for i in range (5):
    tempString = "Trial " + str(i + 1) + " how long for 10 oscillations: "
    temp = int(input(tempString))
    TimesForTenOscillations.append(temp)

AveragePeriod = 0

for i in range(5):
    SumOfPeriods += TimesForTenOscillations[i] / 10

AveragePeriod = SumOfPeriods / 5   

mass = 0.5
distance = 0.14
g = 9.81

Inertia = (mass * g * distance * (AveragePeriod ** 2)) / (4 * (3.14 ** 2)) - (mass * (distance ** 2))

print("The intertia is", round(Inertia, 3))