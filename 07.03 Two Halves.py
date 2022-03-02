from math import ceil

lst = list(str(input("Enter a string: ")))
h = ceil(len(lst) / 2)
r = lst[h:] + lst[:h]
print(''.join(r))