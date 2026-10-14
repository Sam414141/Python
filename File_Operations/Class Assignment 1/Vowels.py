with open("file2.txt",'r') as f:
    count = 0
    for i in f.read().lower():
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    print(f"There are {count} vowel in file")   
    