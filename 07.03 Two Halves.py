from math import ceil

var1 = list(str(input("Enter a string: ")))
h = ceil(len(var1) / 2)
r = var1[h:] + var1[:h]
print(''.join(r))