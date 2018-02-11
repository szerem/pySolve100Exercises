
# with open("countries-new.txt","w") as file_new:
#     with open("countries-raw.txt","r") as file_raw:
#         for line in file_raw:
#             line = line.strip()
#             if len(line) > 2:
#                 file_new.write(line+"\n")

with open("countries-raw.txt","r") as file_raw:
    content = file_raw.readlines()

content = [i.strip() for i in content if len(i) > 2 ]
content = [i for i in content if i != "Top of Page"]

with open("countries-new.txt","w") as file_new:
    for i in content:
        file_new.write(i + "\n")