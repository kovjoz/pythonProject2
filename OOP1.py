

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print("Quack")

    def outlook(self):
        return print("Height: ", self.height, " Weight: ", self.weight)


class Mobile():
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return print(f"mobile phone {self.number} is turned on")

    def turned_off(self):
        return print("mobile is turned off")

    def call(self, number):
        self.called = number
        return print(f"calling {self.called}")


mo1 = Mobile(4443311)
mo1.color = "silk"
"""
mo2 = Mobile(550550)
mo1.turn_on()
mo1.call(889922)
mo2.turn_on()
mo1.turned_off()
mo2.turned_off()
"""

class Demo:
    cnt = 0
    def __init__(self, value):
        self.instance_var = value
        Demo.cnt += 1

    cvar = 1000

print(Demo.cnt)
d1 = Demo(500)
print(Demo.cnt)
d2 = Demo(600)
print(Demo.cnt)

for i in range(5):
    d3 = Demo(i)
Demo.cnt = 11
print(Demo.cnt)
d4 = Demo(2)
print(Demo.cnt)

#help(10)

