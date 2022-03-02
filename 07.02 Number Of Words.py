count = 0
line = str(input("Enter a string: "))
for i in line:
    if(i.isspace()):
        count = count+1

result = len(line.split())

print(str(result) + " words")