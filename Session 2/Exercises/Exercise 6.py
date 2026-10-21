# Steel

SteelYoungsModulus = 200
SteelForce = 8000
SteelRadius = 1.1
SteelInitialLength = 500
SteelCrossSectionalArea = 0
SteelStress = 0
SteelStrain = 0
SteelLengthChange = 0
SteelFinalLength = 0

# Aluminium

AluminiumYoungsModulus = 60
AluminiumForce = 5000
AluminiumRadius = 2.5
AluminiumInitialLength = 750
AluminiumCrossSectionalArea = 0
AluminiumStress = 0
AluminiumStrain = 0
AluminiumLengthChange = 0
AluminiumFinalLength = 0

# Titanium

TitaniumYoungsModulus = 115
TitaniumForce = 4000
TitaniumRadius = 3
TitaniumInitialLength = 1000
TitaniumCrossSectionalArea = 0
TitaniumStress = 0
TitaniumStrain = 0
TitaniumLengthChange = 0
TitaniumFinalLength = 0

DataArray = [[SteelYoungsModulus, SteelForce, SteelRadius, SteelInitialLength, SteelCrossSectionalArea, SteelStress, SteelStrain, SteelLengthChange, SteelFinalLength, "Steel"],
             [AluminiumYoungsModulus, AluminiumForce, AluminiumRadius, AluminiumInitialLength, AluminiumCrossSectionalArea, AluminiumStress, AluminiumStrain, AluminiumLengthChange, AluminiumFinalLength, "Aluminium"],
             [TitaniumYoungsModulus, TitaniumForce, TitaniumRadius, TitaniumInitialLength, TitaniumCrossSectionalArea, TitaniumStress, TitaniumStrain, TitaniumLengthChange, TitaniumFinalLength, "Titanium"]]

for materialData in DataArray:
    materialData[4] = 3.14 * ((materialData[2] / 1000) ** 2)
    materialData[5] = materialData[1] / materialData[4]
    materialData[6] = materialData[5] / (materialData[0] * 10 ** 9)
    materialData[7] = materialData[6] * materialData[3]
    materialData[8] = materialData[3] + materialData[7]
    print("The final length of", materialData[-1], "is", materialData[8], "metres.")