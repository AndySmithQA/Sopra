filename = "wordds.txt"
errmsg = ""
try:
    f = open(filename)
except FileNotFoundError as err:
    errmsg = filename + " not Found"
    print(err.args[1])
except (TypeError,ValueError, OSError):
    errmsg = "Invalid Filename"
else:
    print("Thank you")

if errmsg != "":
    exit(errmsg)