def ProperCase(s):
    str = ''
    str += s[0].upper()
    for i in range(1, len(s)):
        str += s[i].lower()
    s = str
    return s
def RemoveNewLine(s):
    return s.strip('\n')
def Trim(s):
    return s.strip()
def FirstName(s):
    i = s.find(' ')
    return ProperCase(s[0: i])
def LastName(s):
    i = s.rfind(' ')
    return ProperCase(s[i+1 :])
def MiddleName(s):
    first = s.find(' ')
    last = s.rfind(' ')
    if last - first == 0:
        return ""
    elif last - first == 2:
        return ProperCase(Trim(s[first+1:last])) + "."
    else:
        return ProperCase(Trim(s[first+1:last]))

f = open("07.11 Names.txt", "r")
print("%-10s %-10s %-10s" %("First", "Middle", "Last"))
print("%-10s %-10s %-10s" %("----------", "----------", "----------"))

for x in f:
    s = Trim(x)
    s = RemoveNewLine(s)
    print("%-10s %-10s %-10s" %(FirstName(s), MiddleName(s), LastName(s)))