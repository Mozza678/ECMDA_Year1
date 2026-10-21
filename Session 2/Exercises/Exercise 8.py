TimesForTenOscillations = []
for i in range (5):
    tempString = "Trial", i + 1, "how long for 10 oscillations: "
    temp = int(input(tempString))
    TimesForTenOscillations.append(temp)

AveragePeriod = 0

for i in range(5):
    AveragePeriod += TimesForTenOscillations / 50

mass = 0.5
distance = 0.14
g = 9.81

Inertia = (mass * g * distance * (AveragePeriod ** 2)) / (4 * (3.14 ** 2)) - (mass * (distance ** 2))