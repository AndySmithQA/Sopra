import re

# f = open("words.txt.txt", "r")
#
# for line in f:
#     m = re.search(r"^the", line)
#     #m = re.search(r"ing$", line)
#     #m = re.search(r"^[A-Z]", line)
#     #m = re.search(r".", line)
#     #m = re.search(r"[aeiou]{5}", line)
#     #m = re.search(r"^.{20}$", line)
#     #m = re.search(r"^(.)(.)(.).\3\2\1$", line)
#     #m = re.search(r"^(.).*\1$", line)
#     if m:
#         print(line, end="")

# SUB

text = "Always look on the bright side"

x = re.sub("\s", "-", text)

print(x)

line = 'Perl for Python Programmers'

cs, num = re.subn('Perl', 'Python', line)
if num:
    print(cs)

drink = "A glass of Guinness"
if re.search(r"(glass|pint|flaggin) of (Bud|Miller|Guinness)", drink):
    print("time for a beer")












