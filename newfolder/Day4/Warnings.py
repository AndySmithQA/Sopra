# import sys, warnings
#
# warnings.warn("OOOOPS.....\n")
#
# something_nasty = True
# if something_nasty:
#     sys.stderr.write("The program has crashed...")
#     sys.exit("The file ran out of RAM")
#
#
# num = ""
# isaNum = False
# while isaNum == False:
#     num = input("Enter a number")
#     if num.isnumeric():
#         print("Thank you")
#         isaNum = True
#     else:
#         print("That was not a number")
#
# confNum = int(num)
#
# print(f"Number Doubled is {confNum*2}")

# num = input("Enter a number")
#
# try:
#     float(num)
# except ValueError:
#     print("That was not a number")
# else:
#     print("Thank you")
# finally:
#     print("Lets Continue")

# filename = "wordds.txt"
# errmsg = ""
# try:
#     f = open(filename)
# except FileNotFoundError as err:
#     errmsg = filename + " not found"
#     print(err.args[1])
# except (TypeError, ValueError, OSError):
#     errmsg = "Invalid File Format"
# else:
#     print("File Opened....")
#
# if errmsg != "":
#     exit(errmsg)

# raise IOError("Oh Dear")

# def myfunct(*arguments):
#     if not all(arguments):
#         raise ValueError('False or Empty Argument in myfunct')
#
# try:
#     myfunct('Tom', 42, '')
# except ValueError as err:
#     print("Missing or False Data:", err)
#
# print("Continuing......")

class MyError(Exception):
    pass

def myfunct(*arguments):
     if not all(arguments):
         raise MyError('False or Empty Argument in myfunct')

try:
     myfunct('Tom', 42, '')
except MyError as err:
     print("Missing or False Data:", err)








