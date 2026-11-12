import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

thermoData = pd.read_csv("Session 4 - Thermo Lab/Exercises/Exercise 2 (Thermo Lab)/Thermo lab results.csv")

envoironmentArray = thermoData["Envoironment"].to_numpy()
temperatureArray = thermoData["Temperature (K)"].to_numpy()
offsetArray = thermoData["Syringe offset (mm)"].to_numpy()

syringeInternalRadius = 13.3

volumeArray = ((offsetArray - 12.6) / 10) * np.pi * (syringeInternalRadius / 10) ** 2

gradient = (np.sum(volumeArray * temperatureArray)) / (np.sum(temperatureArray ** 2))

print(gradient)
print(volumeArray)

plt.scatter(temperatureArray, volumeArray, label = "Data Points")
plt.axline((260, 260*gradient), (370, 370 * gradient), label = "Best fit line", color = "red")
plt.xlabel("Temperature (K)")
plt.ylabel("Volume (cm^3)")
plt.title("Temperature vs Volume")
plt.legend()

plt.savefig("Session 4 - Thermo Lab/Exercises/Exercise 2 (Thermo Lab)/TemperatureVsVolumeGraph.png", dpi = 400)
plt.savefig("Thermo Lab Report/TemperatureVsVolumeGraph.png", dpi = 400)

plt.show()