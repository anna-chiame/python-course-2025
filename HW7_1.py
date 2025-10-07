# ask user to enter a sentence
sentence = input("Enter a sentence: \n")

# split the sentence into words
words = sentence.split()

#  empty dictionary
word_count = {}

# count occurrences of each word
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)