__author__ = 'shihchosen'
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, my name is', self.name)
p = Person('Chosen')
p.sayHi()