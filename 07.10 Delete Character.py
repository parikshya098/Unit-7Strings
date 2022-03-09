user_string = input("Enter a string: ") 
for i in range(len(user_string)):
    if(user_string[i] != "@"): 
        print(user_string[i], end = "") 