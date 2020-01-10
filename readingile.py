import re

# we don't care about case sensitivity and therefore use lower:
abcfile = open("abc.txt").read().lower()

words = re.findall(r"\b[\w-]+\b", abcfile)
print("Myfile contains to total: " + str(len(words)))

for x in ["the", "of", "on", "to", "this"]:
    print(x + "' occurs " + str(words.count(x)) + " times" )

