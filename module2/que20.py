words = input("Enter a list of words separated by space: ").split()

max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

print("The length of the longest word is:", max_len)