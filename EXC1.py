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

print("new")






