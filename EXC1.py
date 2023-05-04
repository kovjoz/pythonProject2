# https://pynative.com/python-basic-exercise-for-beginners/

# Exercise 2: Print the sum of the current number and the previous number
"""
p = 0
for i in range(10):
    print("current:", i, "previous:", p, "sum:", i+p)
    p = i
"""

# Exercise 3: Print characters from a string that are present at an even index number
"""str1 = list(input("String:"))
l = len(str1)

for c in range(0, l, 2):
    print(str1[c])"""

# Exercise 5: Check if the first and last number of a list is the same
"""
def list_end_chk(chklist):
    if chklist[0] == chklist[-1]:
        return True
    else:
        return False

input_list = input("List:")
print("Given list:", input_list)
print("Result is:", list_end_chk(input_list))
"""
# Fibonacci_1
"""
def fibo(f):
    if f == 1 or f == 2:
        return 1
    if f > 2:
        return (fibo(f-1) + fibo(f-2))

n = int(input("Fibo:"))
for i in range(1, n+1):
    print(fibo(i))
"""

# Fibonacci_2
"""
def fibo(f):
    if f == 1 or f == 2:
        return 1

    if f > 2:
        prev, act = 0,  1
        for x in range(2, f+1):
            prev, act = act, prev + act
        return act

y = int(input("Fibo:"))
for i in range(1, y+1):
    print(fibo(i))
"""
# Create a function with variable length of arguments
"""
def multip(*args):
    result = 1
    for j in args:
        result = result * j
    return result

print(multip(2, 3, 2, 5))
"""

# Recursive adding
"""
def adding(num):
    if num:
        return num + adding(num-1)
    else:
        return 0

number = int(input("Number:"))
print(adding(number))
"""
# Convert two lists into a dictionary
"""
keys = ["ten", "twenty", "thirty"]
values = [10, 20, 30]

d1 = dict(zip(keys, values))
print(d1)
"""
# Get the key of a minimum value from the following dictionary
"""
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75,
    'IT': 100,
    'Art': 64
}
minval = 1000
for k, v in sample_dict.items():
    if v < minval:
        minval = v
        key = k
print(key)
"""
#

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

car1 = Vehicle("Mercedes", 240, 55000)
print(car1.name, car1.max_speed, car1.mileage)


