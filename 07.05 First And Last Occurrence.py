first_index = -1
last_index = -1
word = input("Enter a string: ")

for i in range(len(word)):
    if word[i] == 'f':
        if first_index == -1:
            first_index = i
        last_index = i

if first_index == -1:
    print(0)
elif first_index == last_index:
    print(first_index)
else:
    print(first_index, last_index)