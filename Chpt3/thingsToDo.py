#Thing 1
year_list = [1986, 1987, 1988, 1989, 1990]

#Thing 2
print("Third Birthday:", year_list[3])

#Thing 3
print("Oldest Year:", year_list[-1])

#Thing 4
things = ["mozzarella", "cinderella", "salmonella"]

#Thing 5
things[1] = things[1].capitalize()
print("Is it capital:", things[1])

#Thing 6
things[0] = things[0].upper()
print("Is it all caps", things[0])

#Thing 7
del things[2]
print("All Things:", things)

#Thing 8
surprise = ['Groucho', 'Chico', 'Harpo']

#Thing 9
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print("lowered, reversed, and capitalized:", surprise[-1])

#Thing 10
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print("English to French Dictionary:", e2f)

#Thing 11
print("French for Walrus:", e2f["walrus"])

#Thing 12
f2e = {}
for (key, value) in e2f.items():
    f2e[value] = key

print("French to English Dict:", f2e)

#Thing 13
print("English for chien:", f2e['chien'])

#Thing 14
englishKeysSet = set(e2f.keys())
print("English Keys Set:", englishKeysSet)

#Thing 15
life = {}
life['animals'] = {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}
life['plants'] = {}
life['other'] = {}
print("Life super dict:", life)

#Thing 16
print("Top level keys of life:", life.keys())

#Thing 17
print("animals keys:", life['animals'].keys())

#Thing 18
print("animals-->cat keys:", life['animals']['cats'])