# Python Essentials 1
"""
import sys
import math
import random

# shadowing
def func1():
    z = 1
    print(z)

z = 77
func1()
print(z)

# shadowing feloldás -> global
def func2():
    global y
    y = 10
    print(y)
"""

"""var = 100

if var > 11:
    print(">11")
elif var > 1:
    print(">1")
elif var > 2:
    print(">2")
else:
    print("else")
"""
"""
max = -999999

number = int(input("Number: "))
counter = 0

while number:
    if number > max:
        max = number
    counter += 1
    number = int(input("Number: "))

print(counter, "db szám, ", "max= ", max)
"""
"""
for digit in "0165023":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
else:
    print("always")
    for j in range(1, 4):
        print(j, "always2")
    else:
        print("inner always")
print("main")
"""

"""
#doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

def word_search(documents, keyword):
    # list to hold the indices of matching documents
    index = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            index.append(i)
    return index

#print(word_search(doc_list, 'casino'))

def multi_word_search(documents, keywords):
    out = {}
    for word in keywords:
        l2 = word_search(documents, word)
        out[word] = l2
    return out

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
print(multi_word_search(doc_list, keywords))

import numpy

rolls = numpy.random.randint(low=1, high=6, size=5)
print(rolls)

print(type(rolls))

print(rolls + 10)

"""
"""
list1 = ["b", "c", "ee", "a"]

upper_list = list(map(lambda item: item + 'x', list1))
dict1 = dict(zip(list1, upper_list))
print(dict1)
#print(sorted(dict1.items(), key= lambda x: x[1]))
#print("\n".join("{}:\t{}".format(k, v) for k, v in dict1.items()))
print("\n".join("{}:\t{}".format(k, v) for k, v in sorted(dict1.items(), key= lambda x: x[0])))

src = "c"
for c in list1:
    if c == src:
        break
else: print(" * No ", src, " !")

print(list(range(1,11)))

list2 = [1, 2, 22, 32, 2, 54, 3]
print(list2[::3])
"""
