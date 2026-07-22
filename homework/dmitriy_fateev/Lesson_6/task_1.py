text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
new_text = []

for word in words:
    if word[-1] == ",":
        new_text.append(word[:-1] + "ing" + ",")
    elif word[-1] == ".":
        new_text.append(word[:-1] + "ing" + ".")
    else:
        new_text.append(word + "ing")

print(" ".join(new_text))
