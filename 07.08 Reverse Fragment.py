# Prompt for the String
string = input("Enter a string: ")

# Get the indexes for which there is 'h'
h_index = [i for i in range(len(string)) if string[i] == 'h']

# The first and last index of the list h_index.
h_0, h_1 = h_index[0], h_index[-1]

# Sub setting the string and reversing it
print(string[h_0:h_1+1][::-1])