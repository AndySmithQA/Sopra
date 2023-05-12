# infile = open('country.txt', "r")
#
# print(infile.readline().strip("\n"))
#
# for i in range(10):
#     input("Press Enter")
#     print(infile.readline()) #\n
# infile.close()
# print(infile.readline())
#
# linelist = open('country.txt').readlines()
#
# print(linelist[:2])
#
# for line in open('country.txt', 'r'):
#     if line[0] == 'K':
#         print(line)
#
#
# with open('country.txt', 'r') as file:
#     for line in file:
#         if line[0] == "Z":
#             print(line)


def testerdef():
    print("hi")

#Writing to files
#
# file = open("myfile.txt", 'w')
#
# num = file.write("Goodbye\n")
#
# file.flush()
#
# print(num)
#
# file.writelines(['World\n','What a nice day'])
#
# file.close()
#
# with open("myfile.txt", 'a') as output:
#     num = output.write("Hello")
#     output.writelines(['World\n','What a nice day'])
#
# #Binary Mode
#
# with open('myfile.txt', 'rb') as my_input:
#     for line in my_input:
#         print(line.decode())
#
# #Random Access to a file
#
# fh = open('country.txt', 'rb')
#
# index = {}
#
# while True:
#     line = fh.readline()
#     if not line: break
#     fields = line.decode().split(',')
#     index[fields[0]] = fh.tell() - len(line)
#
# key = 'Nigeria'
#
# fh.seek(index[key])
# print(fh.readline().decode(), end="")
#
# fh.close()
#
# print(index['Nigeria'])
#
# #Pickling - Pickle
#
# import pickle
#
# caps = {
#     'Australia': 'Canberra',
#     'UK': 'London',
#     'Eire': 'Dublin',
#     'US': 'Washington'
# }
#
# outp = open('capitals.p', 'wb')
#
# pickle.dump(caps, outp)
#
# outp.close()
#
# inp = open('capitals.p', 'rb')
#
# caps = pickle.load(inp)
#
# inp.close()
#
# # print(capitalCities)
#
# import shelve
#
# db = shelve.open('capitals')
# #
# # db['UK'] = 'London'
# #
# # db.close()
# #
# # db = shelve.open('capitals')
#
# print(db['UK'])
#
# db.close()
#
# import gzip
#
# outp = gzip.open('capitals.pgz', 'wb')
# pickle.dump(caps, outp)
# outp.close()
#
# inp = gzip.open('capitals.pgz', 'rb')
# caps = pickle.load(inp)
# print(caps)
# inp.close()



















