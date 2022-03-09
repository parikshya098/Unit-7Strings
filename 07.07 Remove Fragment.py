str = input("Enter a string: ")
list = []
for pos,char in enumerate(str):
    if(char == 'h'):
        list.append(pos)
length = len(list)
start_index = list[0]
end_index = list[length-1]
strnew = str[0: start_index:] + str[end_index + 1::]
print(strnew)