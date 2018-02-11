d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "We couldn't find that word!"

word = input("Enter word: ").lower()
print(vocabulary(word))