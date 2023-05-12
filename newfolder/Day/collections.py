#Builtins

mynums = [44,66,12,3,99,3.142,42]

print('Len:', len(mynums))
print('Min:', min(mynums))
print('max:', max(mynums))
print('Total:', sum(mynums))

names = ['Bill','george','donald','dave']

print('Max:', max(names))
print("A" < "a")

#Tuple Operations
# ("hi","Dave")
# Swap

a = 'a'
b = 'b'
print('-' * 10, 'before', '-' *10)

print(f'a = {a}, lives at {id(a)}')
print(f'b = {b}, lives at {id(b)}')

a, b = b,a
print('-' * 10, 'after', '-' *10)
print(f'a = {b}, lives at {id(a)}')
print(f'b = {a}, lives at {id(b)}')

#unpacking
one, two, three = range(5,8)

print(one, two, three)

for i, el in enumerate(['A','B']):
    print(i, el)

names = ['Bill','george','donald','dave']

for name, el in enumerate(names):
    print(name, el)


# nestedNames = [
#     [0,"Bill"],
#     [1,"george"]
# ]
#
# print(nestedNames[1][1])
# mytup = 'a',
# mytup = 'a','b','c'
#
# mytup = mytup * 4
# #mytup *=4
#
# print(mytup)

#Slicing tuples

mytup = ('eggs','bacon','spam','tea', 'beans')

print(mytup)
print(mytup[3:5])
print(mytup[-2])

print(mytup[1:])
print(mytup[:2])

#Assignment
# *rest
matrix = ('eggs','bacon','spam','tea', 'beans', 'pie')

first, second, *rest = matrix

print(first, second, rest)

first, *middle, last = matrix

print(first, middle, last)

for first, *middle, last in matrix:
    print(first, middle, last)

#LISTS
#Adding
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(hex(id(cheese)))

cheese.append('Wensleydale')
print(cheese)
print(hex(id(cheese)))

cheese[2:2] = ['Chester', 'Ilchester']
print(cheese)

cheese.extend(['Oke', 'Devon Blue'])
print(cheese)

cheese.insert(3,['Brie', 'Edam'])
print(cheese)
#
# runners = [
#     ["Dave",25,24,27],
#     ["Kate",44,55,66]
# ]
#
# #Remove by Position
saved = cheese.pop(0)
print(cheese)
print(saved)

del cheese[:]
print(cheese)

while cheese:
    saved = cheese.pop()
    print(saved)

#Sorting
cheese = ['Cheddar', 'Stilton', 'Oke','Cornish Yarg']

cheese.sort(key=len, reverse=False)
print(cheese)

nums = ['1001', '34', '3', '77', '42', '9']

nums.sort(key=int)
print(nums)

newstr = sorted(nums)
newnum = sorted(nums, key=int)
print(newstr)
print(newnum)

# #Sets
s1 = { 5,6,7,8,5}
print(s1)
s2 = set([9,10,11,12,9])
print(s2)
s3 = frozenset([9,10,11,12,9])
print(s3)
s4 = {22,33,44,55}
s5 = {11,55,66,77}
print("{} {}".format(s4,s5))

s4.remove(22)
s5.add(22)
print("{} {}".format(s4,s5))
#
cheese = ["edam", "brie", "cheddar", "edam"]

cheese = list(set(cheese))

print(cheese)

s6 = {'A', 'B', 'C', 'D'}

s7 = {'C', 'D', 'E', 'F'}

print(s6 & s7) # Intersection (entries in both)
print(s6 | s7) #Union (All items in both sets)
print(s6 - s7) #Differrence (Items in s6 but not in s7
print(s6 ^ s7) #SymetricDifference (items that occur in one set only)

#Dict methods

# my_dict = {
#     'Name': 'Bob',
#     'Age': 45
# }

mydict = {
    'UK': ['London', 'Manchester', 'Norwich'],
    'US': ['Miami', 'Boston', 'New York']
}
print(mydict['UK'][1])

redsox = 1
print(mydict['US'][redsox])

mydict['FR'] = ['Paris', 'Lyon', 'Bordeaux']
print(mydict)

for country in mydict.keys():
    print(country, ":", mydict[country])

del mydict['FR']
print(mydict)

mydict.pop('US', -1)

mydict['UK'].append('Macclesfield')

country = {
    'SP': ['Madrid', 'Barcelona']
}

mydict.update(country)

nebulas = {
    'M42': 'Orion',
    'C33': 'Veil',
    'M8': 'Lagoon'
}

items = nebulas.keys()
print(items)