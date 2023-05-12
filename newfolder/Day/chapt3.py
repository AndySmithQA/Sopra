# #Truth
#
# print(10 == 10)
# print( 9 < 9)
# print("hell" in "hello")
#
# print("9" + "8")
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = num1 + num2
# print(f"Those numbers added together is {num3}")
#
# print(bool(0))
# print(bool(1))
#
# myList = []
#
# print(bool(myList))
#
# print(bool([1]),bool([0]))
#
# #Selection
# age =  int(input("Enter your Age: "))
#
# if age > 17:
#     print("You are welcome")
# elif age == 17:
#     print("Come back next year")
# else:
#     print("You must leave, you are underage")
#     print("Go away")
# #
# lista = ['green', 'eggs', 'ham']
# listb = ['eggs', 'green', 'ham']
#
# if lista == listb:
#     print("same")
#
# if "eggs" in lista:
#     print("It has Eggs")
#
# if "green" in lista:
#     print("With Envy")
#
# print(id(lista[0]) == id(listb[1]))
#
# tuple1 = (1,)
# tuple2 = (1,)
# print(tuple1, tuple2)
#
# print(tuple1 is tuple2)
# print(tuple1 == tuple2)
#
# print("An" not in "Andy")
#
# print(True + True + False)
#
# #AND - Both elements must be true
# #
# uname = "Bill"
# pword = ""
# if uname:
#     print("Username is present")
#
# if pword:
#     print("Password is present")
#
# if pword and uname:
#     print("All data exists")
#
# if pword or uname:
#     print("Some data exists")
#
#
#
# if 0 < number < 42 < distance:
#     print("Within Tolerances")
#
# if number < 42 and number > 0:
#     if distance < 42:
#         print("Within Tolerances")
#     else:
#         print("Distance too long")
# else:
#     print("Problem with number")
#
# myList = [0,1,2,3]
#
# if all(myList):
#     print("All were True")
#
# if any(myList):
#     print("Some were True")
# #
# #Iteration
# #FOR Loop - Unconditional
#
# for i in range(1,11):
#     print(i)
#
# myList = [0,1,2,3]
#
# import sys
#
# args = sys.argv
#
# print(args[0])
#
# for idx, arg in enumerate(myList, start=1):
#     print('Index:', idx, 'Argument:', arg)

# WHILE Loops - Conditional Loops

# number = 10
#
# while number > 5:
#     print(number)
#     number -= 1
#
# print("Loop Finished")


attempts = 0
pin = 1234
success = False

while attempts < 3:
    testPin = int(input("Enter your pin"))
    if testPin == pin:
        success = True
        break
    else:
        attempts += 1
        print("That was incorrect")
        print(f"Remaining attempts = {3 - attempts}")

print("Thank you")
if success:
    print("You are logged on")
else:
    print("You are locked out")


score = int(input("Enter your Score"))

if score < 1 or score > 100:
    print("Invalid number")
else:
    if score > 90:
        print("You got an A*")
    elif score > 80:
        print("You got an A")
    else:
        print("You failed")









