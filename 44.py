import string

# a = range(0, len(string.ascii_lowercase),2)
# b = range(1, len(string.ascii_lowercase),2)

# with open("43.txt", "w") as f:
#     for aa, bb in zip(a,b):
#         f.write("{}{}\n".format(string.ascii_lowercase[aa],string.ascii_lowercase[bb]))

with open("44.txt", "w") as f:
    for a,b,c in zip( string.ascii_lowercase[0::3], 
                    string.ascii_lowercase[1::3],
                    string.ascii_lowercase[2::3]): 
        f.write(a+b+c+"\n")