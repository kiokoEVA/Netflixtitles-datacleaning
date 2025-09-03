#this program is used to check whether a given case is upper case or lower case
# ask for user input
char= input("Kindly input a character: ")
# the logic to check whether the character is upper case or lower case
if char.isupper():
    print(f"The character {char} is an upper case letter.")
else:
    print(f"The character {char} is a lower case letter.")
    
# Display the result
