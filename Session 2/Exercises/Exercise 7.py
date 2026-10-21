velocity = int(input("What is the velocity in metres per second? "))
density = float(input("What is the density in kilograms per metre cubed? "))
angle = int(input("What is the angle between the aerofoil and the horizontal? "))

dynamicPressure = 0.5 * density * velocity ** 2
liftCoefficient = 2 * 3.14 * angle

liftForce = dynamicPressure * liftCoefficient

print("The lift generated is", str(round(liftForce, 2)) + "N")