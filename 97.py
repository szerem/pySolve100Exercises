file = open("user_data.txt", "a+")

while True:
    line = input("Napisz cos:")
    if line == "SAVE":
        file.close()
        file = open("user_data.txt", "a+")
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line+"\n")