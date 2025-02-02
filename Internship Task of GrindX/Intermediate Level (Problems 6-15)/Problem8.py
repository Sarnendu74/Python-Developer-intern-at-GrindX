# Initialize string
text = "Hello world ! Hello everyone"
word_count = dict()
# Initializing an empty string to each build words
word = ""
# Looping through each character in the string
for char in text:
    if char != " ":
        word += char
    else:
        if word != "":
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            word = ""
print(word_count)