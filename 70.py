import requests

r = requests.get("http://www.pythonhow.com/data/universe.txt")
text = r.text
# i = 0
# for t in text:
#     if t == "a":
#         i += 1


i = text.count("a")
print(i)



