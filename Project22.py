
"""
# CIPHER
message = input("Enter a message: ")
cipher = ""

message = message.upper()
for ch in message:
    if not ch.isalpha():
        continue
    code = ord(ch) + 1
    if chr(code) > "Z":
        code = ord("A")
    cipher += chr(code)

print(cipher)
"""
"""
# PALINDROM
pali1 = input("Mi a mondat: ")

pali2 = pali1.replace(" ", "")
pali3 =pali2.upper()
list1 = list(pali3)
list2 = []

for x in list1:
    list2.insert(0, x)
print(list1)
print(list2)

pali = True
i = 0
while pali and i < len(list1):
    if list1[i] == list2[i]:
        i += 1
        pali = True
    else:
        pali = False

print(pali)
"""

"""
# interval read, exception handling
def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("wrong input")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("not in the range: " + str(min), "..", str(max))
    return value

test = read_int("Enter a number: ", -10, 10)
print("Selected: ", test)
"""

class Stack:
    def __init__(self):
        self.__stacklist = []

    def push(self, val):
        self.__stacklist.append(val)

    def pop(self):
        val = self.__stacklist[-1]
        del self.__stacklist[-1]
        return val

class SumStack(Stack):
    def __init__(self):       # Subclass Constructor
        Stack.__init__(self)       # Superclass's Constructor
        self.__sum = 0

    def push(self, val):       # override
        self.__sum += val
        Stack.push(self, val)  # push method from the Superclass

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum

class CountStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__popcounter = 0

    def get_counter(self):
        return self.__popcounter

    def pop(self):
        Stack.pop(self)
        self.__popcounter += 1

class Fifostack():
    def __init__(self):
        self.fifolist = []

    def fifoin(self, val):
        self.fifolist.append(val)

    def fifoout(self):
        elem = self.fifolist[0]
        del self.fifolist[0]
        return elem



"""
fifo1 = Fifostack()
for i in range(1,4):
    fifo1.fifoin(i)

for j in range(1,3):
    print(fifo1.fifoout())

# print(Fifostack.__dict__)
# print(fifo1.__dict__)

"""



class Snakes:
    long = 5.5
    def __init__(self):
        self.__sound = "sss"

    def get_sound(self):
        return self.__sound


class Python(Snakes):
    def __init__(self):
        super().__init__()
        self.__venomous = True
        self.long = 7.7
        self.dist = 0

    def get_venom(self):
        return self.__venomous

    def __str__(self):
        info = f"venom= {self.__venomous}, long= {self.long} "
        return info

    def __inner__(self):
        print("can't touch")

    def distance(self):
        self.dist += 1





"""
sn1 = Snakes()
print("Snakes sound: ", sn1.get_sound())

sn2 = Python()
print("Python venom: ", sn2.get_venom())
print("Python sound: ", sn2.get_sound())
"""


"""
st1 = SumStack()

for i in range(5):
    st1.push(i)
    print("sum: ", st1.get_sum())

for j in range(1,4):
    st1.pop()
    print("pop sum", j, ": ", st1.get_sum())
"""

class Test:
    c = 2
    def __init__(self, val):
        self.d = 8
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 0
"""
for i in range(1,10):
    tt = Test(i)
    if hasattr(tt, 'a'):
        print(i, ": a= ", tt.a)

    if hasattr(tt, 'b'):
        print(i, ": b= ", tt.b)
"""
"""
print(hasattr(Test, 'a'))
print(hasattr(Test, 'b'))
print(hasattr(Test, 'c'))
print(hasattr(Test, 'd'))
print(Test.__dict__)
tt = Test(3)
"""



"""
print("------------------".center(20))
for i in range(1, 6):
    t1 = Test(i)
    try:
        print("a= ", t1.a)
    except AttributeError:
        pass

    try:
        print("b= ", t1.b)
    except AttributeError:
        pass
print("OK")
"""
"""
#2.14.8
hour = int(input("Hány óra? "))
alarm = int(input("Alarm hány óra múlva? "))
alarm_hour = (hour + (alarm % 24)) % 24
print("Alarm időpont: ", alarm_hour)
"""
"""
# Lab: HH:MM:SS increase/decrease seconds

class Timer:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second =second

    def __str__(self):
        if self.__hour < 10:
            h_info = f"0{self.__hour}:"
        else:
            h_info = f"{self.__hour}:"

        if self.__minute < 10:
            m_info = f"0{self.__minute}:"
        else:
            m_info = f"{self.__minute}:"

        if self.__second < 10:
            s_info = f"0{self.__second}"
        else:
            s_info = f"{self.__second}"

        return h_info + m_info + s_info

    def next_second(self):
        self.__sum_time = 3600 * self.__hour + 60 * self.__minute + self.__second
        if self.__sum_time == (23 * 3600) + (59 * 60) + 59:
            self.__hour = 0
            self.__minute = 0
            self.__second = 0
        else:
            self.__sum_time += 1
            self.__hour = self.__sum_time // 3600
            self.__minute = (self.__sum_time - (3600* self.__hour)) // 60
            self.__second = self.__sum_time - (3600* self.__hour) - (60* self.__minute)


    def prev_second(self):
        self.__sum_time = 3600 * self.__hour + 60 * self.__minute + self.__second
        if self.__sum_time == 0:
            self.__hour = 23
            self.__minute = 59
            self.__second = 59
        else:
            self.__sum_time -= 1
            self.__hour = self.__sum_time // 3600
            self.__minute = (self.__sum_time - (3600 * self.__hour)) // 60
            self.__second = self.__sum_time - (3600 * self.__hour) - (60 * self.__minute)


time1 = Timer(7,59,57)
#print(time1.__str__())

for i in range(5):
    time1.next_second()
    print(time1.__str__())

print("-------------")
for i in range(5):
    time1.prev_second()
    print(time1.__str__())

"""
"""
# Lab: Weeker

class WeekDayError(Exception):
    def __init__(self):
        print("Wrong day")


class Weeker:
    __week = ['Mon','Tue','Wed','Thu', 'Fri', 'Sat','Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__week.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__week[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + (n % 7))

    def sub_days(self, n):
        self.__current = (self.__current - (n % 7))


weekday = Weeker('Mon')
print(weekday)
weekday.add_days(15)
print(weekday)
weekday.sub_days(23)
print(weekday)

"""
"""
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.get_x(), point.get_y())

class Triangle:
    points = [0,0,0,0,0,0]

    def __init__(self, v1, v2, v3):
        Triangle.points[0] = v1.get_x()
        Triangle.points[1] = v1.get_y()
        Triangle.points[2] = v2.get_x()
        Triangle.points[3] = v2.get_y()
        Triangle.points[4] = v3.get_x()
        Triangle.points[5] = v3.get_y()


    def perimeter(self):
        self.a = math.hypot(abs(Triangle.points[0] - Triangle.points[2]), abs(Triangle.points[1] - Triangle.points[3]))
        self.b = math.hypot(abs(Triangle.points[2] - Triangle.points[4]), abs(Triangle.points[3] - Triangle.points[5]))
        self.c = math.hypot(abs(Triangle.points[0] - Triangle.points[4]), abs(Triangle.points[1] - Triangle.points[5]))
        return self.a + self.b + self.c


t1 = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(t1.perimeter())

"""
"""
def reci(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("cannot")
    else:
        print("OK")
    finally:
        print("End of TRY")
    return n

print(reci(4))
"""
"""
import math


def derek(a, b, c):
    #c1 = (a ** 2 + b ** 2) ** 0.5
    l1 = [a, b, c]
    l1 = sorted(l1)
    a1 = l1[0]
    b1 = l1[1]
    c = l1[2]
    c1 = math.sqrt(a1*a1 + b1*b1)
    d1 = abs(c - c1)   #floating point comparision
    print(d1)
    print(l1)
    if d1 <= 0.00001:
        return True
    else:
        return False

print(derek(1.0, 1.414213, 1.0))
print("------")
print(derek(5.0,3.0,4.0))
"""
"""
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("  | " * (nest-1), end="")
    if nest > 0:
        print("  +--", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)
"""
"""
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'piedone', 'napoli']:
        raise PizzaError(pizza, "no such pizza")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza is ready")

for (pz, ch) in [("piedone", 0), ("napoli", 110), ("napolo" , 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ": ", tmce.cheese)
    except PizzaError as pe:
        print(pe, ": ", pe.pizza)
"""
"""
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end="! ")

import math

try:
    print(math.pow(2))
except TypeError:
    print("A")
else:
    print("B")
    
"""
"""
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')


class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()"""

# Yield **************
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(11))
print(fibs)
print(fibs[-1])


"""list1 = []
for x in range(5):
    list1.append(10 ** x)
print(list1)

list2 = [10 ** ex for ex in range(6)]
print(list2)
"""
"""
list1 = [0 if x % 2 == 0 else 1 for x in range(5)]  # list + iteration
print(list1)

for v in (0 if x % 2 == 0 else 1 for x in range(8)):  # generator (no list)
    print(v, end=", ")
"""
"""
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')

#def poly(x):
#    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
"""
"""
first = list(input("First: "))
last = list(input("Last: "))
first.reverse()
last.reverse()
print("".join(last), "".join(first))
"""
"""
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=" ")
print()

list_3 = [1,3,4,5,90]
list_4 = list(map(lambda x: 3 * x, list_3))
print(list_4)
"""
"""
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc

    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

print("---------------")

def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of

square = nth_power(2)
cube = nth_power(3)

print(square(3), " ", cube(4))

print("---------------")
x = int(input("number: "))
print("1" if x == 1 else "2")
"""
"""
def foo(g, x):
    return g(x)

print(foo(lambda x: x ** 0.5, 9))

short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.upper(), short_list))
print(new_list)

class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.pos) == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]


vowels = Vowels()
for v in vowels:
    print(v, end=' ')

any_list = [1,2,3,4]
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)

"""
"""
 "C:\\Users\\jkovacs\\Desktop\\T1.txt"
f = open("/Users/jkovacs/Desktop/T1.txt", "rt")

for data in f:
    print(data, end="")

f.close()

f2 = open("/Users/jkovacs/Desktop/T1.txt", "at")
f2.write("T3")
f2.close()
print()
print("-----------")

def mltp(*args):
    n = 1
    for a in args:
        n = n * a
    print(n)

mltp(2,3,4)

with open("/Users/jkovacs/Desktop/T1.txt", "wt") as f3:
    f3.write("T4")


with open("/Users/jkovacs/Desktop/T1.txt", "rt") as f4:
    for data in f4:
        print(data, sep="")

"""
"""class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 2
        return current

nums = MyRange(1, 7)
for num in nums:
    print(num)
"""
"""import random

pinr = random.randint(1000, 10000)
print("Random PIN: ", pinr)
#pin = int(input("What is your PIN code: "))

def myrange(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1

nums = myrange(1000,10000)
for num in nums:
    if num == pinr:
        break
print("Your PIN is: ", num)

"""
"""from os import strerror

try:
    cc = lc = 0
    for line in open('C:\\Users\\jkovacs\\Desktop\\T1.txt', "rt", encoding = "utf-8"):
        lc += 1
        for char in line:
            print(char, end="")
            cc += 1
    print("\nChars: ", cc, "\nLines: ", lc)
except IOError as e:
    print("I/O error: ", strerror(e.errno))


try:
    fo = open('C:\\Users\\jkovacs\\Desktop\\T2.txt', "wt")
    for i in range(3):
        fo.write("Line # " + str(i) + "\n")
    fo.close()
except IOError as e:
    print("I/O error: ", strerror(e.errno))


data = bytearray(12)
data2 = bytearray(11)

for i in range(len(data)):
    data[i] = 12 - i

try:
    bf = open('C:\\Users\\jkovacs\\Desktop\\B1.bin', "wb")
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error ", strerror(e.errno))

try:
    bf = open('C:\\Users\\jkovacs\\Desktop\\B1.bin', "rb")
    data = bytearray(bf.read())
    #bf.readinto(data2)
    bf.close()

    for j in data:
        print(hex(j), end=", ")
except IOError as e:
    print("I/O error ", strerror(e.errno))"""

"""
from os import strerror


hszt = {}
path = "C:\\Users\\jkovacs\\Desktop\\"

file = input("File name: ")
try:
    fh = open(path + file, "rt", encoding="utf-8")
except IOError as e:
    print("I/O error ", strerror(e.errno))


for line in fh:
    for ch in line:
        ch = ch.lower()
        if ch.isalpha():
            #print(ch)
            if ch in hszt:
                hszt[ch] += 1
            else:
                hszt[ch] = 1

hszt2 = dict(sorted(hszt.items(), key=lambda item: item[1]))
for (k, v) in hszt2.items():
    print(k, "->", v)

"""
"""from datetime import date
from datetime import datetime
from datetime import time

day1 = datetime(2020,11,4,14,53,0)
print(day1)
print(day1.strftime('%y/%B/%d %H:%M:%S %p'))
print(day1.strftime('%a, %Y %b %d'))
print(day1.strftime('%A, %Y %B %d'))
print(day1.strftime('weekday: %w'))
print(day1.strftime('Day of the year: %j'))
print(day1.strftime('Week number of the year: %U'))

t = time(14, 39)
print(t.strftime("%H:%M:%S"))"""
"""import calendar

#print(calendar.calendar(2021))
#calendar.prmonth(2021, 7)

#cc = calendar.Calendar()

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, y, w):
        self.y = y
        self.w = w
        count = 0
        for i in range(1,13):
            for data in self.monthdays2calendar(y, i):
                if data[w][0] != 0:
                    count += 1
        return count
                #print(data)


c = MyCalendar()
yyear = int(input("Year: "))
wweek = int(input("Weekday: "))

print(c.count_weekday_in_year(yyear, wweek))



#for data in c.monthdays2calendar(2020, 12): print(data)


"""
"""
def my_fun():
    for num in range(3):
        yield num

for i in my_fun():
    print(i)

print(my_fun())
"""
"""my_tuple = (0,1,2,3,4,5,6)
foo = list(filter(lambda x: x-1 and x-0, my_tuple))
print(foo)"""

"""
my_list = [0,1,2,3,4,5,6]
foo2 = list(filter(lambda x: x-1, my_list))
print(foo2)

citylist = ["Roma", "Pisa", "Bari"]

for i, city in enumerate(citylist):
    print(i, city)
""""""
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v

for x in I():
    print(x, end="")
"""
"""
try:
    raise Exception
except Exception:
    print("b")
except BaseException:
    print("a")
except:
    print("c")"""
"""
def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in my_fun(2):
    print(x, end='')
"""
"""class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(A, C))
"""
"""class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B, A):
    def c(self):
        self.a()


s = open("C:\\Users\\jkovacs\\Desktop\\T1.txt", "rt")
print(s.read(1))
"""
"""
import random
a = random.randint(0, 100)
b = random.randrange(10, 100, 3)
c = random.choice((0, 100, 3))
print(a, b, c)"""
"""
numbers = [i*i for i in range(5)]
print(numbers)
foo = list(map(lambda x: x % 2, numbers))
print(foo)
foo = list(filter(lambda x: x % 2, numbers))
print(foo)

"""
"""
from datetime import datetime

dt1 = datetime(2019, 11, 27, 11, 27, 22)
dt2 = datetime(2019, 11, 27, 0, 0, 0)
print(dt1-dt2)"""
"""try:
    raise Exception (1, 2, 3)
except Exception as e:
    print(len(e.args))
"""

"""except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")
""""""
from datetime import timedelta

delta = timedelta(weeks=1, days=7, hours=11)
print(delta * 2)
"""
# List zip function ***************
"""
x_list = [1, 2, 3]
y_list = [2, 4, 6]
z_list = [10, 20, 30]

for x, y, z in zip(x_list, y_list, z_list):
    print(x, y, z)"""