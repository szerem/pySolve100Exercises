d = {"a": 1, "b": 2, "c": 3}
s = dict((k,v) for k, v in d.items() if v <= 1)
print(s)
