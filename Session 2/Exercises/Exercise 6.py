# Steel

SteelYoungsModulus = 200
SteelForce = 8000
SteelRadius = 1.1
SteelInitialLength = 500
SteelCrossSectionalArea = 0
SteelStress = 0
SteelStrain = 0


# Aluminium

AluminiumYoungsModulus = 60
AluminiumForce = 5000
AluminiumRadius = 2.5
AluminiumInitialLength = 750

# Titanium

TitaniumYoungsModulus = 115
TitaniumForce = 4000
TitaniumRadius = 3
TitaniumInitialLength = 1000

DataArray = [[SteelYoungsModulus, SteelForce, SteelRadius, SteelInitialLength],
             [AluminiumYoungsModulus, AluminiumForce, AluminiumRadius, AluminiumInitialLength],
             [TitaniumYoungsModulus, TitaniumForce, TitaniumRadius, TitaniumInitialLength]]

for materialData in DataArray:
    materialData