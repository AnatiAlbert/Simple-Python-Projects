# Code Generator

# TODO 1: input text from user
message = input("Enter your message: ").lower()

# TODO 2: replace each letter with another
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x", "y", "z"]

word = []
for text in message:
    if text in alphabets:
        new = alphabets.index(text)
        new += 1
        new_text = alphabets[new]
        word.append(new_text)
        new_word = "".join(word)

# TODO 3: output the 'encoded' message
print(new_word)
