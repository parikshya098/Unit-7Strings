user_string = input("Enter a string: ") # Prompt the user to enter a string.

# Loop that checks each letter in the user's string.
for i in range(len(user_string)):
    if(user_string[i] != "@"): # IF condition that only prints out letters that are '@'
        print(user_string[i], end = "") # Prints the letters in one line, with no space.