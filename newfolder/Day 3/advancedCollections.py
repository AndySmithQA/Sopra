


# for customers in ls:
#     if customers >= 1:
#         print(customers)

# print(lambda arg : arg >= 1)

# ls = [0,0,1,2] * 10
# iterator = filter(lambda cust: cust >= 1, ls)
#
# for iteree in iterator:
#     print(iteree)

#
import builtins
# import re
#

# for error in filter(lambda string : 'Error' in string, names):
#     print(error)
#
# for name in filter(lambda string : string.startswith('I'), names):
#     print(name)
#
# for name in filter(lambda x: re.search(r"t$",x), names):
#     print(name)
# #
# names = dir(builtins)
# new_list = []
# for name in names:
#     if name.startswith('E'):
#         new_list.append(name)
#
# print(new_list)
#
# new_list = [name for name in names if name.startswith('E')]
#
# print(new_list)
# #
# numbers = list(range(100))
# print([number for number in numbers if number % 2 == 0])

#GENERATORS

# a = range(5)
#
# print(list(a))

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
# # for i in infinite_sequence():
# #     print(i, end=" ")
# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# fruit = ['Apple', 'Pear', 'Orange']
#
# lunch = fruit[:]
#
# lunch[1] = 'Eggs'

# print('fruit:',fruit, '\nlunch:', lunch)

# fruit = ['Knife','Spoon',['Apple', 'Pear', 'Orange']]
# lunch = fruit[:]
# lunch[2][1] = 'Eggs'
# print('fruit:',fruit, '\nlunch:', lunch)

import copy
fruit = ['Knife','Spoon',['Apple', 'Pear', 'Orange']]
lunch = copy.deepcopy(fruit)
lunch[2][1] = 'Eggs'
print('fruit:',fruit, '\nlunch:', lunch)








