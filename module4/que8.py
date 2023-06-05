#Write a python program to find the longest words.
word_list = ['akshita', 'banana', 'charmi', 'dhruv']
longest_word = " "
for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)
  
