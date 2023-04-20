# PCEP test

# Which character is used to separate multiple python statements when placing in a single physical line?
# \
for i in range(2): \
        print(i)

# What refers to assignment of no value in Python?
# None
empty = None
print(empty)

# precedence
print(19 % 4 + 15 / 2 *3)    # 25.5
print(17 / 2 % 2 * 3 ** 3)   # 13.5

# output?
dictionary = {"one": "two", "three": "one", "two": "three"}
v = dictionary["one"]   # "two"

for k in range(len(dictionary)):
    v = dictionary[v]
    print(k, v)

print(v)  # "two"

# output?
print("-"*20)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return      # None !

# print(fun(fun(2)) + 1)  # TypeError because None + 1
print(fun(fun(2)))   # None

# Practise exams *****************************************************
# ********************************************************************

# Practice Exam 1
# 13:46
# 1B, 2D, 3A, 4D, 5D, 6A, 7D, 8A, 9D, 10A
# 11C, 12B, 13B, 14C, 15C, 16B*, 17D, 18C, 19B, 20C
# 21A*, 22C, 23A, 24D, 25B*, 26A, 27C*, 28D, 29A, 30A
# 26 / 30 --> 87%
#
# there can be 2 returns but only the FIRST will run:
def func_trick(a, b):
    return a * b
    return a + b

print(func_trick(2, 3))

list1 = [1, 2, 3, 4, 5, 6, 7]
print("1:", list1[:])   # all items
print("11:", list1[:2])  # from begin to second element = 0,1 indexes
print("12:", list1[:0])  # from begin to first element = empty list!
print("13:", list1[:-2])  # from begin to -2 element
print("14:", list1[1:-1])  # from index 1 to last element
print("141:", list1[3:7])  # from index 3 to end, index 7 !!!
print("142:", list1[3:])   # from index 3 to end
print("143:", list1[3:102]) # again from index 3 to end index 102 valid !!!
print("15:", list1[-1:2])  # empty list!
print("16:", list1[-3:-1])  # from index -3 to -1
print("17:", list1[1:])  # from index 1 to last item inclusive
print("18:", list1[-2:])  # from index -2 to last item inclusive
print("2:", list1[::])  # all items, from begin to end inclusive
print("3:", list1[::1])  # all items, slice step 1
print("4:", list1[::2])  # all items, slice step 2
#print("4:", list1[::0])  # ! ValueError: slice step cannot be 0
print("5:", list1[::-1])  # all items, slice step -1, REVERSE ORDER
print("6:", list1[:-1])   # from begin to last element, all except last one
print("7:", list1[::-2])  # reverse, from the end, with step 2
print("8:", list1[::-3])  # reverse, from the end, with step 3




#  no swap: The function swaps the values of x and y within its
# scope but does not return anything. The values of x and y remain unchanged.
def swap(x, y):
    z = x
    x = y
    y = z
x = 5
y = 10
swap(x, y)
print("swap1:", x, y)

# swap2 with global, return is not necessary
def swap(xx, yy):
    global x
    global y
    z = xx
    x = yy
    y = z
    #return x, y

x = 5
y = 10
swap(x, y)
print("swap2:", x, y)


#  practise exam2
# 21:39
# 1D, 2B, 3A, 4A, 5C, 6D, 7C, 8D, 9C, 10B*
# 11B, 12B, 13B, 14C, 15D*, 16C, 17D, 18A, 19D, 20B
# 21A*, 22A, 23C, 24C, 25A*, 26B, 27C, 28C*, 29A, 30D*
# 24 / 30 --> 80%

list2 = ["a", "b", ""]
print(len(list2))
print(list2)
list2.remove("a")
print(list2)

a = 0b1011
b = 0b1001
print(bin(a ^ b))


print(1 == 1.0)    # True !!! must be seen the Value
print(10/5)        # 2.0 Doch

sample1 = "string example one"
print("Capitalize: ", sample1.capitalize())
print("Title: ", sample1.title())

def greeting(name='"s"'):
    print("Hello", '"', name, '"')

greeting()

print("a", sep="--")     # sep will not be printed
print("a", "b", sep=None) # None = space = default separator
print(end='', sep="--")  # nothing will be printed
print("", "b", sep="--") # --b will be printed
print(end="*")           # * will be printed!
print()
print("Python"*2, sep="--")  # sep will not be printed! It counts only 1 argument.
print(3*"Python"*2)

val = 5
print("this") if val < 50 else print("that")   # Valid! Like list comprehension. Ternary operator.

def fun(a=3, b=2):
    return b ** a

print(fun(2))    # can be called with 1 param

# Test 3
# 18:12
# 1A, 2C*, 3D, 4C, 5B*, 6D*, 7A*, 8B*, 9A, 10A*
# 11C, 12A, 13A, 14D, 15D, 16D, 17B, 18B, 19C*, 20A
# 21D, 22C, 23A, 24C, 25B, 26A, 27C*, 28C, 29B, 30D*
# 21/30 --> 70%


# The *val declaration means that the functions expects multiple arguments.
# When calling myprint function, one can pass in any number of arguments.
# Arguments will be passed to the function as a tuple and printed.
def fun2(*val):
    print(type(val))

a = 2
b = "3"
c = [4]
fun2(a,b,c)

# When bool() is provided an empty list, an empty string or the value 0 as an
# argument, it returns False. The expression will evaluate to True when bool () is
# given any other value, including negative numbers.

print(bool(-1))   # True
print(bool([]))   # False
print(bool(" "))  # space  - True
print(bool(""))   # empty string  - False

# The is operator is an identity operator, it checks whether both the operands
# refer to the same object or not.
# The p and q have equal values, stored in the same memory location, hence p and
# q are same. You can use id() function to check if the variables are same:
# print(id(p)) print(id(q)) which will indicate the same ID for both variables.

p = 10
q = 10
print("p is q? 1:")
print(id(p), id(q), p is q)     # True !

# BUT !
p = 10
q = 10.0
print("p is q? 2:")
print(id(p), id(q), p is q)     # False!
print(p == q)                   # True !

# The range(-2) does not generate any numbers
print(list(range(2)))   # [0, 1]
print(list(range(-2)))  # empty list!

list3 = ["a", "b", "c"]
all = list(range(-2)) + list3
print(all)

# The list contains two elements, and when multiplied by 5, we are
# repeating the same elements 5 times. Therefore the length of the new list is 10.
lst5 = [0, 1] * 5
print("len=", len(lst5), lst5)

# Test4
# 14:15
# 1A, 2A*, 3A, 4A*, 5C, 6A, 7D, 8AC, 9B, 10C
# 11B, 12B, 13A, 14A, 15A, 16D*, 17A, 18A, 19C, 20B
# 21D, 22C, 23B, 24C, 25A, 26B, 27B, 28A, 29B*, 30A
# 26 / 30 --> 87%


def func(mylist):
    mylist[3] = "strawberries"

lst = ["bananas","apples","pears","peas"]
func(lst)
print(lst)


def func2(myparam):
    myparam = "strawberries"

var1 = "bananas"
func2(var1)
print(var1)

def func3(var):
    var = False

bool1 = True
func3(bool1)
print(bool1)

def func4(dic):
    dic[1] = "overwrite"

mydict = {1: "read", 2: "pop"}
func4(mydict)
print(mydict)


# EQUALITY *******************************************************************
# The dictionaries store data in key-value format, hence the comparison
# between two dictionaries is on the basis of key value pairs having the same
# positions, and not solely on the values.
dict1 = {"John":1234, "Fruit":"Apples"}
dict2 = {"Fruit":"Apples", "John":1234}
print("Dictionary:")
print(dict1 == dict2)

tupi1 = (1,2,3)
tupi2 = (1,2)
tupi3 = 3,
tupi4 = tupi2 + tupi3
print("Tuple: ")
print(tupi1 == tupi4)

def funny(listparam):
    listparam[2] = 100

mylist = [1, 2, 3]
funny(mylist)
print(mylist)


for i in range(3):
    print("i=", i)
    for j in range(2):
        if j == 1:
            break
        else:
            print("j=", j)

# The function is expecting at least one positional argument and the rest as
# multiple-arguments, they are treated as a tuple!
def fun(data, *num):
    print(data)
    print(data, num)

fun(3, 2, 1, "a")

# Test 5
# 17:40
# 1A, 2B, 3C, 4A, 5BD, 6B, 7A, 8D, 9A, 10B,
# 11C, 12A, 13D,  14D, 15C, 16B, 17A, 18D, 19A*, 20A
# 21D, 22C, 23D, 24A*, 25C*, 26A, 27B, 28C, 29A, 30D*

# In the function definition, **names is used to pass a keyworded, variablelength
# argument (name-value pairs). The names.items() will return both key and
# value of each pair.
def fun(**names):
    for key, value in names.items():
        print(key, value, end=" ", sep=":")

fun(NAME="Robert",AGE=29, CITY="Dar es salaam")


# *args = collects positional arguments in a tuple
# ** kwargs = collects keyword arguments in a dictionary

print("*args, **kwargs")
def my_func(*args, **kwargs):
    print("Hello world", args, kwargs)
    for item in kwargs.items():
        print(item)             # dictionary item as tuple

my_func("abc", "abc", 123, "abc", key=123, abc=123)


# Test 6
# 21:22
#  1D*, 2D, 3B, 4B, 5B, 6C, 7D, 8A, 9B, 10B
# 11B, 12B, 13B, 14D, 15B, 16A, 17A, 18B, 19C*, 20B
# 21A, 22D, 23B, 24C, 25C, 26D, 27CD*, 28B, 29B, 30A
# 27 / 30 -> 90%

# sorted to tuple is valid
print("-"*20)
tupl = ("d", "a", "e")
print(sorted(tupl))

# The capitalize() function will re-write the word by capitalizing the first
# letter, and keeping the rest of letters in lower-case. Hence, the result is 'Hello'.
print("-"*20)
str1 = "Hello"
str2 = "HeLLo"
print(str1 == str2.capitalize())
print(str2.capitalize())


# The extend() method used on a list adds the elements of the specified list
# provided as an argument to the end of the current list. Hence ones stores [1, 11,
# 111] and is printed out by the first print statement.
# However, the extend() function does not return anything, it operates on the list
# on which it was used (ones). Hence ones_again stores the value of None.
print("-"*20)
ones = [1]
ones_again = ones.extend([11, 111])
print("ones:", ones)
print("ones_again:", ones_again)


# In the for loop, the first iteration fetches "apples", right? Usually we set
# this element on to a local variable - like for f in fruits where the f is the local
# variable. But in this case what we are doing is a bit weird - we are setting it to a
# variable called fruits[-1]. Now what is fruits[-1]. Isn't this accessing the element
# from the fruits list at -1th position? Exactly! That is, we are actually setting the
# first element fetched during the first iteration ("apples") to fruits[-1] which is
# nothing but the last element - this means we are replacing the "cherries" to
# "apples"!! We are actually MODIFYING the main list by running this for loop
# and assigning it to that local variable!
print("-"*20)
fruits = ["apples", "cherries"]

for fruits[-1] in fruits:
    print(fruits[-1], end="|")

print()
print(fruits)


# The variable radius is expecting an integer, however the user entered a
# float (1.0).
# The int(input()) type casting fails.
#error:  r = int(input("r="))
#fixed:  r = int(float(input("r= ")))

# test 7
# 13:57
#  1A, 2B, 3B, 4C, 5C, 6C, 7B, 8D, 9A, 10C
# 11C, 12A*, 13D, 14A, 15C, 16B, 17B, 18D, 19C, 20A
# 21C, 22A, 23A, 24B, 25C, 26C, 27A, 28B, 29A, 30A


# test 8
# 15:10
#  1B, 2D*, 3A, 4A, 5B, 6D, 7B, 8C, 9B, 10A
# 11D, 12B, 13B*, 14B, 15B, 16C, 17B, 18D, 19D, 20B
# 21D, 22A, 23D, 24D, 25C, 26D, 27C, 28B, 29C, 30D

# end= parameter is defined, so next print on the same line
print("titanic", "was", "a", "huge", "ship", sep="*",end="|")
print("but", "sadly","it","sank")


# test 9
# 12:11
#  1C, 2A, 3A, 4B, 5B, 6C, 7A, 8B, 9B, 10A
# 11D, 12A, 13B, 14C, 15B, 16A, 17B, 18A*, 19A, 20A
# 21A, 22A, 23A, 24C, 25D, 26D, 27c, 28d, 29a, 30b*



# test 10
# 23:00
#  1B, 2A, 3A, 4C, 5C, 6A, 7B*, 8D, 9C, 10C
# 11D, 12B, 13A, 14A, 15C, 16C, 17A, 18D, 19C, 20D
# 21C, 22A, 23A, 24A, 25C, 26C, 27CD, 28A, 29CD, 30B


print(0xA + 0xB + 0xC)

# 
from functools import reduce
nums = [
    [2, 2, 13, 15],
    [30, 45],
        ]
res = []
for i in nums:
    r = reduce(lambda x, y: x + y, i)
    res.append(r)
print(res)


# function can read y, and can return y
y = 55
def wow():
    return y
print(wow())   # 55


# String literal separated by whitespace are allowed. They are
# concatenated.
print('new' 'line')














