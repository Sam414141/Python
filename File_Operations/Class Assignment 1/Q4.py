with open("file2.txt", "r") as f:
    words = f.read().split()
    print(f"File has {len(words)} words")
    print(f"Unique Words : {set(words)}")

