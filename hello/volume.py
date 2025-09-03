# Ask the user to input the radius
radius= float(input("Kindly input your desired radius for the sphere: "))

# Calculate the volume using the formula (4/3)πr³
volume=(4/3) * 3.14159 * (radius ** 3)


# Display the result
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")
