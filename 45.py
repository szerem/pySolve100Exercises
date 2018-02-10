import os, string

if not os.path.exists("letters"):
    os.makedirs("letters")

for letter in string.ascii_lowercase: 
    with open("letters/{}.txt".format(letter), "w") as f:
        f.write(letter)