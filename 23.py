from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

print(d["b"][2])

for k,v  in d.items():
    print("{0} has value {1}".format(k, v))
