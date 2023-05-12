# print("€")
#
# euro = "\u20ac"
#
# print(euro)
#
# dollar = "\N{dollar sign}"
# print(dollar)
#
#
# print("This is a string", dollar)

# print(1,2,3, sep=":::::::", end=" ", file="output.txt")
# print(4,5,6)

##Escape Characters

# print("Andy \nSmith \t Here today")

# print("""
#                     89874##fdsjakjh89
#     fgjhsdfg8 gsjh kjhk j98 ~~~~d;fslf
#     dsfj jf'fdsjk '#'
#
#     <tr> This is a row
#         <td>CONTENTS</td>
#     </tr>
# """)

#methods

mynum = "66"

myNewVar = int(mynum)
print(myNewVar)

print(len(mynum))
print("ANDY".lower())

word = "This is a setence"

print(word.replace("set", "sen"))
print(word)

words = "hjdhfui      "
words.rstrip()

print(word.find("is"))
#
# pasword  = "LetMeIn1"
# symbs = "^&%@{:"
# for chars in passwors:
#     if chars.isalpha():
#         .islower()
#         .isupp()
#         in symbols
# if pasword.startswith("L"):

# var1 = "Hello"
# var2 = 56.78474
# var3 = 3676


planets = {
    'Mercury': 57.91,
    'Venus'  : 108.2,
    'Earth'  : 149.597870,
    'Mars'   : 227.94
}

for i,key in enumerate(planets.keys()):
    print(f"{i:2d} {key:<10s} {planets[key]:06.2f} GM")

text = "Remarkable bird, the Norwegian Blue"

print(text[3:8])

#split and Join

line = 'root::0:0:superuser:/root:/bin/sh'

elems = line.split(":")

print(elems)

newline = "@".join(elems)
print(newline)






