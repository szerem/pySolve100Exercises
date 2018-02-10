import string

# a = range(0, len(string.ascii_lowercase),2)
# b = range(1, len(string.ascii_lowercase),2)

# with open("43.txt", "w") as f:
#     for aa, bb in zip(a,b):
#         f.write("{}{}\n".format(string.ascii_lowercase[aa],string.ascii_lowercase[bb]))

with open("43.txt", "w") as f:
    for a,b in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]): 
        f.write(a+b+"\n")