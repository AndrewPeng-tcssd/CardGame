asdf = "hi"
a2 = list(asdf)
lit = ["hi"]
if asdf in lit:
    print("yes")

word = "asdf"
new = ""

for i in range(len(word)):
    new += word[0:len(word)-i]
print(new)