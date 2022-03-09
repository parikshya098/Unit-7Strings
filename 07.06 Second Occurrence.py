input = input("Enter a string: ")
index = -1
count = 0
for i in range(0,len(input)):
    if input[i] == 'f':
        count = count+1;
        index = i
    
if count == 2:
   print(index)
elif count == 1:
    print("One f")
elif count == 0:
    print("Zero f")