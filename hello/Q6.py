# Initialize an empty list
numbers = []

# Loop 
for i in range(5):
    value = int(input(f"Enter value {i+1}: "))
    numbers.append(value)

# Calculate average
average = sum(numbers) / len(numbers)

# Display the result
print(f"The average of the entered values is: {average}")
