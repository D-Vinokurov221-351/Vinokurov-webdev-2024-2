#f = open(example.txt)
words = f.split(" ")
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

for word in words:
    if len(word) == len(longest_word):
        print(word, end = " ")
