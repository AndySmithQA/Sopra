#!/usr/bin/python

# Example Python script

import sys

print(sys.argv)

argc = len(sys.argv)

if argc > 1:
    print('Too many args')
else:
    where = 'World'
    print("Hello", where)

print('Goodbye from ' + 
      sys.argv[1])
