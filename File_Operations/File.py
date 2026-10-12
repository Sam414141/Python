with open("file1.txt", "r") as file:
    lines = file.readlines()
    
    # Access the 4th line directly
    fourth_line = lines[3] 
    print(fourth_line)  # .strip() removes trailing newlines (\n)
