# def mortgage():
#     sal = int(input("Enter salary: "))
#     mort = sal * 5
#     return mort
#
# def output():
#     return "This is from a Function"

# def greeting(name):
#     return f"Good Morning {name}"
#
# print(greeting("Dave"))

# def greeting2(name, age):
#     return f"Good Morning {name}, you are {age} years old"
#
# ageInput = int(input("Enter your age"))
#
# print(greeting2("Frank", ageInput))

# def add(num1, num2):
#     res = num1 + num2
#     return f"Those numbers added together is: {res}"

# def add(val, times):
#     return f"{val} times {times} is: {val * times}"
#
# print(add(4,7))
#
# print(add(6,8))


# def change_list(inlist, val, times):
#     inlist += val * times
#
# mylist = []
#
# change_list(mylist, "F", 9)
#
# print(mylist)

#Default Parameter
#KWARGS returns a DICTIONARY
# def print_vat(**kwargs):
#     print(kwargs)
#
# print(print_vat(gross=150, vatpc=20, message="Your Purchase"))

#Passing Parameters

# def my_funct(*, file, dir, user='root'):
#     print('file: {:}, dir: {:}, to: {:}'.format(file,dir,user))
#
# #by position
# my_funct(file='one','two','three') # file works as it's named
#
# #by default
# my_funct('one','two') # neither work as they are not named
#
# #by name
# my_funct(file='one',dir='two', user='three')# all are named and work

#Variadic Functions
#No fixed number of parameters


# def my_funct(a,b,c):
#     print(a,b,c)
#
# mytup = 23,45,67
# print(my_funct(*mytup))

#*args   AGRS RETURNS TUPLE
# def my_funct(dir, *args):
#     print('dir:', dir, 'Files:', args)
#
# print(my_funct('C:/Sopra','f1.txt','f2.txt','f3.txt','f3.txt','f3.txt','f3.txt'))

#Variables in Functions
#GLOBAL

# interest_rate = 3 #GLOBAL VARIABLE
# def scope_test():
#     interest_rate = 4 #LOCAL VARIABLE
#
#     print('Function before:', interest_rate)
#     interest_rate = 42 # changing the global
#     print('Function after:', interest_rate)
#
# scope_test()
# print('Global:', interest_rate)

# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         def innerinner():
#             nonlocal x
#             x = 3
#             print('innerinner:', x)
#         innerinner()
#         print('inner:', x)
#     inner()
#     print('Outer:', x)
#
# x = 0
# outer()
# print('Global:', x)

#Docstrings

# def my_funct():
#    '''
#    myfunct has no parameters and prints Hello!
#    :return:
#    '''
#    return "Hello"
#
# help(my_funct)

# #lambda
#
# def f(x):
#     return x * 2
#
# print(f(2))
#
# g = lambda x : x * 2
#
# print(g(2))
#
# ls = ['109', '102972', '23', '5', '000082']
#
# ls.sort(key = lambda x : int(x) )
#
# print(ls)

compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)

x = 32
y = 3

print("a > b", compare(x,y))


