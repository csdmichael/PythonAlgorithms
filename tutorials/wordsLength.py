sentence = "this is a sentence"
word_lengths = []
words = sentence.split()
for word in words:
    word_lengths.append(len(word))
print(words)
print(word_lengths)