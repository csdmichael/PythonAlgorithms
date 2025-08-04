sentence = "this is a sentence"
word_lengths = []
words = sentence.split()
for word in words:
    word_lengths.append(len(word))
print(words)
print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
#newlist = []
#for x in numbers:
#    if x > 0:
#        newlist.append(int(x))
print(newlist)