# This program converts the hours of a given number of days to seconds

# User input
days = int(input("Kindly enter the number of days: "))

# Logic to convert days to seconds
seconds = days * 24 * 60 * 60

print(f"{days} day(s) is equal to {seconds} seconds.")
