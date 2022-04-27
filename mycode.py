#!/usr/bin/bash/python

import math
import collections
from collections import deque
import sys

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cypher = deque(letters)
count = int(sys.argv[1])
for i in range(int(count)):
  a = cypher.popleft()
  cypher.append(a)
code = {}
for i in range (len(letters)):
  code[letters[i]] = cypher[i]
string = ''
b = str(sys.argv[2])
count = 0
for j in str(b):
  if j.isalpha():
    c = j.capitalize()
    d = code[c]
    string += d
    count+=1
  if count == 5:
    string += ' '
    count = 0

print(string)