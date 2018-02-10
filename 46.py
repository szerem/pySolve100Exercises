import os, glob


letters = []
file_list = glob.glob("letters/*.txt")

# print(file_list)
for file_path in file_list:
    with open(file_path,"r") as file_to_read:
        letters.append(file_to_read.read().strip())


print(letters)