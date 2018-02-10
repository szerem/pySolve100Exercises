import string
with open("41.txt", "w") as f:
    for c in string.ascii_letters:
        f.write("{}\n".format(c))