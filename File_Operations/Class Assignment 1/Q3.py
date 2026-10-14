sen = input("Enter a sentence :")
l = sen.split()
long = ""
for i in l:
    if len(i) > len(long):
        long = i
    
print(f"Longest word :{long}")  