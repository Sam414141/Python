#Replace wovels
nm = "sumit"
s = []
for i in nm.lower():
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        s.append("z")
    else:
        s.append(i)
print("".join(i for i in s))