#Returns a properly cases string s by uppercasing the first character
# and lowercasing the rest of the string.
def ProperCase(s):
    str = ''
    str += s[0].upper()
    for i in range(1, len(s)):
        str += s[i].lower()
    s = str
    return s

#Returns a string with the NewLine Character ("\n") removed from string s
def RemoveNewLine(s):
    return s.strip('\n')

#Returns a string with the leading and trailing spaces removed from string s
def Trim(s):
    return s.strip()

#Returns the first name of string s
def FirstName(s):
    i = s.find(' ')
    return ProperCase(s[0: i])

#Returns the last name of string s
def LastName(s):
    i = s.rfind(' ')
    return ProperCase(s[i+1 :])

#Returns the middle name of string s
def MiddleName(s):
    first = s.find(' ')
    last = s.rfind(' ')
    if last - first == 0:
        return ""
    elif last - first == 2:
        return ProperCase(Trim(s[first+1:last])) + "."
    else:
        return ProperCase(Trim(s[first+1:last]))


#Open the file
f = open("07.11 Names.txt", "r")

print("%-10s %-10s %-10s" %("First", "Middle", "Last"))
print("%-10s %-10s %-10s" %("----------", "----------", "----------"))

#Read file line by line
for x in f:
    s = Trim(x)
    s = RemoveNewLine(s)
    print("%-10s %-10s %-10s" %(FirstName(s), MiddleName(s), LastName(s)))