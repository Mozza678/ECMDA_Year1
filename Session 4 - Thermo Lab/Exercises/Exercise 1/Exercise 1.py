import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

diameter = 10 * 10 ** -3
length = 50 * 10 ** -3

forceDisplacementData = pd.read_csv("Session 4 - Thermo Lab/Exercises/Exercise 1/ForceDisplacementAl.csv")

forceArray = forceDisplacementData["Force (kN)"].to_numpy()
displacementArray = forceDisplacementData["Displacement (mm)"].to_numpy()

crossSectionalArea = np.pi * (diameter / 2) ** 2

stressArray = forceArray * (10 ** 3) / crossSectionalArea

strainArray = displacementArray * 10 ** -3 / length

plt.plot(strainArray, stressArray)
plt.xlabel("Strain")
plt.ylabel("Stress")
plt.savefig('Session 4 - Thermo Lab/Exercises/Exercise 1/StressStrainGraph.png', dpi=400)

print("The maximum tensile stress is", round(np.max(stressArray), -6), "N")
print("The maximum strain is", round(np.max(strainArray), 3))

stressStrainDataFrame = pd.DataFrame({'Stress':stressArray, 'Strain':strainArray})

stressStrainDataFrame.to_csv("Session 4 - Thermo Lab/Exercises/Exercise 1/StressStrain.csv", index = False)

plt.show()